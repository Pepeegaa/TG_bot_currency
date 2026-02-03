import time

_cache = {}

def get_from_cache(key: str, ttl: int):
    record = _cache.get(key)

    if not record:
        return None

    value, timestamp = record

    if time.time() - timestamp > ttl:
        del _cache[key]
        return None

    return value

def set_cache(key: str, value):
    _cache[key] = (value, time.time())