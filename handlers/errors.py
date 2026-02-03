from aiogram import Router
from aiogram.types import ErrorEvent
import logging

router = Router()
logger = logging.getLogger(__name__)

@router.errors()
async def error_handler(event: ErrorEvent):
    logger.exception(
        "Unhandled exception",
        exc_info=event.exception
    )
    return True  # ❗ критично