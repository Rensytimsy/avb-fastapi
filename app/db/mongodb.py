from beanie import init_beanie
from motor import motor_asyncio
import asyncio
from ..config import Settings
import os

db_url = os.getenv("MONGO_URL")
db_name = "UrlShortener"

client = motor_asyncio.AsyncIOMotorClient(db_url)
db = client[db_name]

#Initialize beanie

async def init_db():
    from .mongoModel import Users, UrlRedirect
    await init_beanie(
        database=client[db_name],
        document_models=[Users, UrlRedirect]
    )
    print("Database connected successfully")
    
#test mongodb connectivity
async def test_connection():
    try:
        await client.admin.command("ping")
        print("Mongo connection successfull")
        return True
    except:
        print("Mongo connection unsuccessfull")
        return False
    
def get_client():
    return client    

if __name__ == "__main__":
    asyncio.run(test_connection())