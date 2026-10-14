"""Compatibility entry point; bot.py also serves the HTTP health checks."""

import asyncio

from bot import start_bot


if __name__ == "__main__":
    asyncio.run(start_bot())
