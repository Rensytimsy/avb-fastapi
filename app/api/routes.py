from fastapi import APIRouter, HTTPException, responses
import requests
import pyshorteners
from pydantic import BaseModel, HttpUrl
from app.urlShortener import shorten_url
from beanie import Document, init_beanie
from motor import motor_asyncio
import os
from app.db.mongoModel import Users, UrlRedirect
from app.db.mongodb import init_db, init_beanie

"""
Motor and beanie are some powerful tools that are used to interact with mongodb
"""

class Url(BaseModel):
    original_url: str
    short_url: str
    
class NewUser(BaseModel):
    name: str
    age: int
    department: str

client = motor_asyncio.AsyncIOMotorClient(os.environ["MONGO_URL"])
database = client.get_database("ShortUrl")
db_collections = database.get_collection("Url")


#I am using pydantic to send a request body to our server for url shortening    
class RequestUrl(BaseModel):
    url: str

#Tags as used in apirouter specifies our api endpoints tags
router = APIRouter(tags=["hello", "more-info"])

#Below are some api endpoints, that return data
@router.get("/get-data")
async def get_hello():
    try:
        print(help(url_shortener))
        response = requests.get("https://fakestoreapi.com/products")
        products = response.json()
        
        # print(products)
        return({"found-products" : f"{products}"})

    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail=f"Something went wrong when fetching data {err}")


#Below route enpoint gets more info on our project
@router.get("/more-info/{name}")
async def more_info(name: str):
    return({"Message": f"Hello {name}, more information on this project will appear here!, once uploaded"})


#Below is the url shortener api route
@router.post("/shorten-url")
async def url_shortener(url: Url):
    try:
        if not init_beanie():
            return
        
        #The code below shortens the url from the web
        shortened_url = shorten_url.shorten_url(url.original_url)
        await init_db()
        
        #create an object of url shorteners
        new_short_url = UrlRedirect(
            original_url=url.original_url,
            short_url=shortened_url
        )
        
        await new_short_url.insert()
        
        return({
            "Success": True,
            "url-info": new_short_url
        })
        
    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail=f"Something went wrong while trying to shorten url: {err}")


@router.get("/url-redirect/{url_code:path}")
async def url_redirect(url_code: str):
    try:
        found_url = await UrlRedirect.find_one(UrlRedirect.short_url == url_code)
        if not found_url:
            raise HTTPException(status_code=404, detail="Url does not exist, not found")
        
        #If the url is present in the database just return the url and redirect the user to the orginal url
        
    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail=f"Error: {err}")
    
    return responses.RedirectResponse(found_url.original_url)    

    
@router.get("/simple-url/{url}")
async def get_hashed_url(url: str):
    return

#Create a user
@router.post("/create-user")
async def create_user(user: NewUser):
    #First make sure that beanie has been initialized
    if not init_beanie():
        return
    
    #If beanies is initialized one can successfully create documents
    await init_db()
    new_user = Users(
        name=user.name,
        age=user.age,
        department=user.department
    )
    
    #create document by inserting one
    await new_user.insert()
    
    #return a response after user has been created
    return ({
        "Success" : True,
        "created_user" : new_user
    })
    
    