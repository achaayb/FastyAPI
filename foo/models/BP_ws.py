from fastapi import WebSocket
from ..databases.redis import pubsub_1, sub_1, connections_db, connections_cnt_db
import asyncio
import json

"""TODO [] multiserver ws connections
    - we cant pickle the websocket connection (ikr)
    - [x] configure redis
    - [x] use redis pub/sub to broadcast a message to each worker wich then broadcasts
        to connections list
"""

"""DOCS
    - redis pub/sub : https://itnext.io/event-data-pipelines-with-redis-pub-sub-async-python-and-dash-ab0a7bac63b0
    - scaling redis : https://redis.io/docs/manual/scaling/
    - list[dict] search : https://stackoverflow.com/questions/5426754/google-python-style-guide
    - aioredis commands : https://aioredis.readthedocs.io/_/downloads/en/v1.3.0/pdf/
    - aioredis hashes : https://aioredis.readthedocs.io/en/v1.3.0/mixins.html?highlight=hash#hash-commands
    - [] redis pool : https://www.programcreek.com/python/example/98950/aioredis.create_redis_pool
    - dict mapping : https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
"""


ws_schema = {
        "type" : "object",
        "properties": {
            "context": {"type": "string"},
            "method": {"enum": ["GET", "POST", "PATCH", "DELETE"]},
            "message": {"enum": [
                {"broadcast": {"type": "string"}, "message": {"type": "string"}},
                {"private": {"type": "string"}, "message": {"type": "string"}, "uid": {"type": "string"}}
            ]
        }
    },"required": ["context", "method", "message"]
}

class ConnectionManager:
    def __init__(self):
        #dumb to use it like this in prod.
        #use redis or something idk, wait for next push.
        self.connections = {}

    async def connect(self, websocket: WebSocket,uid: str,uuid: str):
        await websocket.accept()
        await connections_db.hincrby(uid, uuid, 1)
        if not uid in self.connections: self.connections[uid] = [websocket]
        else: self.connections[uid].append(websocket)

    async def broadcast_self(self, data: str): #needed for local broadcast [WORKING]
        print("broadcast_self data > ",data)
        print("broadcast_self data ? ",type(data))
        def connections_generator():
            for conn in self.connections.values():
                yield conn
        for con_dict_obj in connections_generator():
            print("broadcast_self all > ",list(con_dict_obj))
            for i in iter(con_dict_obj):
                print("broadcast_self iter > ",i)
                await i.send_text(data)
    async def broadcast_all(self,data: str): #needed for global broadcast [WORKING]
        #get all uuid then broadcast to uuid
        print("broadcast_all > ", data)
        print("broadcast_all ? ", type(data))
        uuid_set = await connections_cnt_db.smembers("uuid")
        for uuid in uuid_set:
            await pubsub_1.publish(uuid, data)
    async def broadcast_private(self,uid: str, message: str): #needed for private broadcast []
        foo = await connections_db.hgetall(uid)
        print("broadcast_private hgetall > ", foo)
        print("broadcast_private hgetall ? ", type(foo))
        for i in foo:
            await pubsub_1.publish(i, message)
        #await pubsub_1.publish(uuid,message)
    async def send_private(self,uid: str, message: str):
        for conn in iter(self.connections[uid]):
            await conn.send_text(message)


    async def disconnect(self,uid: str, uuid: str, websocket: WebSocket):
        if not int(await connections_db.hincrby(uid, uuid, -1)):
            await connections_db.hdel(uid,uuid)
        self.connections.pop(uid)

manager = ConnectionManager()