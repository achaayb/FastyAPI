import aioredis
from os import environ

connections_db = aioredis.from_url(f"{environ['REDIS_URI']}/0", decode_responses="utf-8") #users and its machines uuid
connections_cnt_db = aioredis.from_url(f"{environ['REDIS_URI']}/1", decode_responses="utf-8") #machines list
pubsub_1 = aioredis.from_url(f"{environ['REDIS_URI']}", decode_responses="utf-8") # reserved for PubSub communication
sub_1 = pubsub_1.pubsub()