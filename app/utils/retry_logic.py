import asyncio
import functools
from app.core.logger import logger
import random
from typing import Callable, Type, Tuple, Optional

def async_retry(
    max_attempts: int = 3,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
    backoff_base: int = 2,
    backoff_factor: float = 1.0,
    jitter: bool = True,
    logger_prefix: str = "Retrying",
):
    """
    Generic async retry decorator with exponential backoff and optional jitter.

    Args:
        max_attempts (int): Max number of retry attempts.
        exceptions (tuple): Exceptions that trigger a retry.
        backoff_base (int): Base of the exponential backoff.
        backoff_factor (float): Multiplier for backoff delay.
        jitter (bool): Whether to add random jitter to backoff time.
        logger_prefix (str): Prefix to include in log messages.
        logger (logging.Logger): Optional logger to use.

    Returns:
        Callable: Wrapped function with retry logic.
    """

    log = logger 

    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return await func(*args, **kwargs)
                except exceptions as e:
                    is_final = attempt == max_attempts
                    if is_final:
                        log.error(f"{logger_prefix}: Attempt {attempt} failed. No more retries.", exc_info=True)
                        raise
                    delay = backoff_factor * (backoff_base ** (attempt - 1))
                    if jitter:
                        delay *= random.uniform(0.8, 1.2)
                    log.warning(f"{logger_prefix}: Attempt {attempt} failed with {e.__class__.__name__}: {e}. "
                                f"Retrying in {delay:.2f}s...")
                    await asyncio.sleep(delay)
        return wrapper
    return decorator