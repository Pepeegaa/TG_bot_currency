from TG_bot_currency.API.retryy import get_json_with_retry
from TG_bot_currency.API.cashing import get_from_cache, set_cache

async def get_usd_to_rub(api_key: str) -> float | None:
    cache_key = "usd_rub"
    cached = get_from_cache(cache_key, ttl=300)

    if cached:
        return cached

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

    data = await get_json_with_retry(url)

    if not data:
        return None

    rate = data["conversion_rates"]["RUB"]
    set_cache(cache_key, rate)
    return rate