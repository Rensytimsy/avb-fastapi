from fastapi import FastAPI, HTTPException
from app.config import cache_data
from app.api.routes import router
from beanie import Document, init_beanie
from motor import motor_asyncio
import requests
from contextlib import asynccontextmanager
import os
from app.db.mongodb import get_client, init_db

#Asynccontextmanager to ensure that db is only initialized once on application start
@asynccontextmanager
async def life_span(app: FastAPI):
    await init_db()
    yield
    get_client().close()

#Below is a fastapi app function initialization, the function returns a fastapi application
def create_fastapi_application() -> FastAPI:
    app = FastAPI(
        title="Simple fast api application",
        lifespan=life_span
    )
    
    
    #below line of code makes sure, that the app use routes_middleware to load/use routes
    app.include_router(router, prefix=cache_data().api_prefix)
    
    #Invoke the db initialization instance in here so that whenever the app starts the method is triggered
    
    #finally return the app so that whenever the function is triggered it return the fastapi application that has been created
    return app

#finnally initialize the application
app = create_fastapi_application()


#default routes that will render to guide users on this project
@app.get("/")
def guidance_info():
    return({
        "name" : "Simple flask application",
        "greetings-route" : "/api/v1/get-data",
        "more-info" : "/api/v1/more-info/your name",
        "url-shortener" : "/api/v1/url-shortener"
    })
    