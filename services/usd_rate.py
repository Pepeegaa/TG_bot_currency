import aiohttp
from typing import Optional

CBR_URL = "https://www.cbr-xml-daily.ru/daily_json.js"


async def get_usd_rate(session: aiohttp.ClientSession) -> Optional[float]:
    try:
        async with session.get(CBR_URL) as response:
            response.raise_for_status()
            data = await response.json()
            return data["Valute"]["USD"]["Value"]

    except aiohttp.ClientError as e:
        print(f"[API ERROR] {e}")
        return None
