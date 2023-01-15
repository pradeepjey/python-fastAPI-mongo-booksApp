
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
from json_encoder import bson_to_json

async def find_one(db: AsyncIOMotorClient, collection: str, query: any):
    row = db[collection]
    result = await row.find_one(query)
    if result != None:
        return bson_to_json(result)
    else: 
        return result

async def find_query(db: AsyncIOMotorClient, collection: str, query: any, filter: any, size: int, sort: any):
    result: List[any] = []
    row = db[collection]
    rows = row.find(query).sort(sort).limit(size)
    async for row in rows:
        result.append(bson_to_json(row))
    return result

async def patch_update_one(db: AsyncIOMotorClient, collection: str, filter_query: any, data: any):
    row = db[collection]
    result = await row.update_one(filter_query, { "$set": data })
    return result

async def search_by_text(db: AsyncIOMotorClient, collection: str, txtQuery: str, filter: any, sort: any):
    result: List[any] = []
    row = db[collection]
    rows: any
    print(txtQuery)
    rows = row.find({"$text": { "$search": txtQuery}}, filter).sort(sort).limit(1000)
    async for row in rows:
        result.append(bson_to_json(row))
    return result

async def name_search(db: AsyncIOMotorClient, collection: str, query: any, filter: any, size: int, sort: any):
    result: List[any] = []
    row = db[collection]
    rows = row.find({"name": { "$regex": "^"+ query, "$options":"i" }}).sort(sort).limit(size)
    async for row in rows:
        result.append(bson_to_json(row))
    return result
