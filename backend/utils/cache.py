import aioredis

redis = aioredis.from_url("redis://localhost")

async def cache_query(query, result=None):
    if result:
        await redis.set(query, result, ex=3600)  # Cache for 1 hour
        return
    return await redis.get(query)
