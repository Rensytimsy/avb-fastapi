from fastapi import FastAPI
from app.config import cache_data
from app.api.routes import router

#Below is a fastapi app function initialization, the function returns a fastapi application
def create_fastapi_application() -> FastAPI:
    app = FastAPI(
        title="Simple fast api application"
    )
    
    #below line of code makes sure, that the app use routes_middleware to load/use routes
    app.include_router(router, prefix=cache_data().api_prefix)
    
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
    