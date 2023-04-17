import asyncio
import os
from aio_pika import connect_robust
from aio_pika.patterns import RPC
from dotenv import load_dotenv
from resolver import resolve
from bestconfig import Config


async def server() -> None:
    load_dotenv()
    rmq = os.environ.get("RMQ")
    __config = Config("settings.ini").to_dict()
    connection = await connect_robust(rmq)

    async with connection:
        channel = await connection.channel()
        rpc = await RPC.create(channel)
        await rpc.register(resolve.__name__, resolve, auto_delete=True)

        try:
            await asyncio.Future()
        finally:
            await connection.close()


if __name__ == "__main__":
    asyncio.run(server())
