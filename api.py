from asyncio import exceptions
from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from db import get_database
from typing import Optional
from actions import  find_one, find_query, name_search, patch_update_one, search_by_text 
from bson.objectid import ObjectId
from model import searchModel


books = APIRouter()

@books.get("/books", tags=["books"])
async def get_books(
    size: int = 20,
    db: AsyncIOMotorClient = Depends(get_database)):
    sort = [("_id", -1)]
    query_data = await find_query(db, "booklist", {}, {}, size, sort)
    return query_data


@books.get("/book/{b_id}", tags=["books"])
async def get_book(
    b_id: str,
    db: AsyncIOMotorClient = Depends(get_database)):
    query = { "_id": ObjectId(b_id)}
    query_data = await find_one(db, "booklist", query)
    return query_data


@books.get("/favourite_books", tags=["books"])
async def get_favourite_books(
    size: int = 20,
    db: AsyncIOMotorClient = Depends(get_database)):
    sort = [("_id", -1)]
    query_data = await find_query(db, "booklist", {"isFavourite": True }, {}, size, sort)
    return query_data

@books.patch("/set_favourite_status/{b_id}/{status}", tags=["books"])
async def set_favourite_status(
    b_id: str,
    status: bool,
    db: AsyncIOMotorClient = Depends(get_database)
    ):
        query = { "_id": ObjectId(b_id)}
        await patch_update_one(db, "booklist", query, {'isFavourite': status})
        return "status updated"
       
@books.post("/book_search", tags=["books"])
async def search_books(
    search : searchModel,
    size: int = 20,
    db: AsyncIOMotorClient = Depends(get_database)):
    sort = [("_id", -1)]
    searchtext = search.txt
    query_data = await name_search(db, "booklist", searchtext, {}, size, sort)
    return query_data
 