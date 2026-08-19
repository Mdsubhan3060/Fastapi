import asyncio

from app.database.connection import engine


async def test_connection():
    async with engine.connect() as connection:
        print("PostgreSQL connection successful")


asyncio.run(test_connection())