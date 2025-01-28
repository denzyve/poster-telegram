from asyncio import run
from pyrogram import Client

api_id = 12345
api_hash = ""

async def main():
    async with Client("my_account", api_id=api_id, api_hash=api_hash, workdir="./output") as app:
        await app.authorize()
        
run(main())
