from fastapi import APIRouter, HTTPException
import requests
import pyshorteners
from pydantic import BaseModel, HttpUrl
from app.urlShortener import shorten_url


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


#Below is the url shortener function
#I will be using pyshortener since is easy to intergrate and work with for simply shortening the urls passes

@router.post("/shorten-url")
async def url_shortener(provided_url: RequestUrl):
    try:
        client_url = provided_url.url
        minimized_url = shorten_url.shorten_url(client_url)
        
        return({
            "message": "Url hashed successfully",
            "success" : True,
            "status": 200,
            "original-url": client_url,
            "short-url": minimized_url
        })
        
    except requests.exceptions.RequestException as err:
        raise HTTPException(status_code=500, detail=f"Something went wrong while trying to shorten url: {err}")
    
@router.get("/simple-url/{url}")
async def get_hashed_url(url: str):
    return