#ws route Boilerplate

"""TODO [] External connecion storage
    - [] redis config
    - [] redis[ws connection] crud
        - [] ws connection metadata
    - [] connection timeout
"""

"""TODO [] ws code optimisation
    - ???
"""

"""TODO [] Testing
    - [] manual
    - [] automated
"""

"""WS REQUEST STANDART
    1) datatype always json
    2) request format
        {
            'method': {GET/POST../},
            'context': {context id},
            'data': {'key': 'value'}
        }
    3) response format
        {
            'context': "context string or id",
            'data': {Response model}
        }
"""

"""DOCS
    UID : https://docs.python.org/3/library/uuid.html#uuid.uuid4
    REDIS DATA TYPES : https://redis.io/docs/manual/data-types/
    REDIS CONTROL : https://redis.io/commands/
    SHUTDOWN : https://stackoverflow.com/questions/68018314/how-do-you-trigger-app-on-eventshutdown-for-fastapi-with-uvicorn
"""

from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect
from ..helpers.response import Response, Error_ws
from ..models.BP_ws import manager
from ..databases.redis import sub_1, pubsub_1, connections_db, connections_cnt_db
import asyncio
import threading
import json
from uuid import uuid4
from ..dependencies import BP_jwt as jwt_dependencies
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from jsonschema import validate

UUID = str(uuid4())

router = APIRouter(
    responses={404: {"description": "Not found"}},
)


"""sub
    - sub function runs in an external thread
    - expected subscribed message format
        - broadcast : {"subject": "subject", "data": "message"}
        - private  : {"to": "to", "subject": "subject", "data": "message"}
"""
async def sub():
    #possible bottlenack requires furhter testing / theorycrafting
    #we're awaiting execution in an event loop that ONLY has one loop. pointless?
    #await sub_1.subscribe('broadcast') probably dont need this.. i optimised i guess
    await sub_1.subscribe(UUID)
    async for i in sub_1.listen():
        if i['type'] == 'subscribe': continue #skip first connection ping
        #if i['channel'] == 'broadcast': #idk why i wrote this earlier.. but whatever
        #    #try: for later
        #    #    foo = json.loads(i['data'])
        #    #except ValueError as e:
        #    #    continue
        #    await manager.broadcast_self(foo)
        elif i['channel'] == UUID: #broadcast_local < from global broadcast
            foo = json.loads(i['data'])
            print("pubsub uuid pre type > ",foo)
            print("pubsub uuid pre type ? ",type(foo))

            if foo['type'] == "broadcast":
                await manager.broadcast_self(json.dumps(foo['data']))
            elif foo['type'] == "private":
                await manager.send_private(foo['data']['uid'], json.dumps(foo['data']))
            #await manager.broadcast_private(user,foo)

def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    asyncio.run_coroutine_threadsafe(sub(), loop)

@router.on_event("startup")
async def startup():
    print(f"uid : {UUID}")
    # broadcast listener in separate thread that contains its own event loop
    loop = asyncio.get_event_loop()    
    t = threading.Thread(target=start_background_loop,args=[loop], daemon=True)
    t.start()
    await connections_cnt_db.sadd("uuid", UUID)

@router.on_event("shutdown")
async def shutdown():
    await connections_cnt_db.srem("uuid", UUID)

@router.websocket("/ws/{token}")
async def websocket_endpoint(websocket: WebSocket, Authorize: AuthJWT = Depends(AuthJWT)):
    #verify JWT token before accepting connection
    token = websocket.path_params['token']
    try:
        Authorize.jwt_required("websocket",token=token)
        foo = Authorize.get_raw_jwt(token)
        jwt_dict = json.loads(foo['sub'])
        if 'username' not in jwt_dict: raise AuthJWTException
        else: uid = jwt_dict['username']
    except AuthJWTException:
        """[] Notify client invalid JWT"""
        """ END """
        await websocket.close()
        return

    await manager.connect(websocket,uid,UUID)
    msg = {"type": "broadcast", "data": {"message": f"User {uid} Joined"}}
    await manager.broadcast_all(json.dumps(msg))
    #await manager.broadcast_private("username","test")
    while True:
        try:
            #data = await websocket.receive_text()
            data = await websocket.receive_text() # if receive_json() is used connection is auto closed
            try:
                data = json.loads(data)
                """[] Validate json"""
                """END"""
            except ValueError:
                """[] Notify user of invalid input"""
                await websocket.send_text(Error_ws("Invalid JSON format"))
                """END"""
                print("invalid json")
                continue
            print("data > ",data)
            if data['type'] == 'broadcast':
                await manager.broadcast_all(json.dumps(data))
            elif data['type'] == 'private':
                print("private data > ",data['data'])
                print("private data > ",type(data['data']))
                #print("private data dumps > ",json.dumps(data))
                #print("private data dumps> ",type(json.dumps(data)))
                await manager.broadcast_private(data['data']['uid'], json.dumps(data))
        except (WebSocketDisconnect):
            msg = {"type": "broadcast", "data": {"message": f"User {uid} Disconnected"}}
            await manager.broadcast_all(json.dumps(msg))
            await manager.disconnect(uid,UUID,websocket)
            break 