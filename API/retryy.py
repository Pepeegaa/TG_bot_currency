import asyncio
import aiohttp
from typing import Optional

async def get_json_with_retry(
    url: str,
    params: dict | None = None,
    retries: int = 3,
    delay: float = 0.5
) -> Optional[dict]:

    timeout = aiohttp.ClientTimeout(total=5)

    for attempt in range(1, retries + 1):
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url, params=params) as response:
                    response.raise_for_status()
                    return await response.json()

        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            if attempt == retries:
                print("❌ All retries failed:", e)
                return None

            await asyncio.sleep(delay * attempt)  # backoff