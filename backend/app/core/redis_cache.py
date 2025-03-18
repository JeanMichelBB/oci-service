import redis
import json

cache = redis.Redis(host="localhost", port=6379, db=0)

async def set_cache(key: str, value: dict, ttl: int = 300):
    cache.setex(key, ttl, json.dumps(value))

async def get_cache(key: str):
    data = cache.get(key)
    return json.loads(data) if data else None