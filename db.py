from motor.motor_asyncio import AsyncIOMotorClient
from typing import Final


mongodb_dbname: Final = "booksApp"
mongodb_user: Final = ""
mongodb_password: Final = ""
mongodb_min_pool_size: Final = 10
mongodb_max_pool_size: Final = 100
mongodb_dsn: Final = f"mongodb+srv://{mongodb_user}:{mongodb_password}@cluster1.jgkoc.mongodb.net/{mongodb_dbname}?retryWrites=true&w=majority"

class DataBase:
    client: AsyncIOMotorClient = None

db = DataBase()

async def get_database() -> AsyncIOMotorClient:
    return db.client['booksApp']

async def connect_to_mongo():
    print("connected")
    db.client = AsyncIOMotorClient(mongodb_dsn,
                                   maxPoolSize=mongodb_max_pool_size,
                                   minPoolSize=mongodb_min_pool_size)


async def close_mongo_connection():
    db.client.close()
    print("connection closed!")