import asyncio
from contextlib import suppress

from bot.utils.launcher import process
from keep_alive import keep_alive

keep_alive()

async def main():
    await process()


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        asyncio.run(main())
