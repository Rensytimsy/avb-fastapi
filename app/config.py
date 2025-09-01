from dotenv import load_dotenv
import os
from functools import lru_cache

load_dotenv()

class Settings:
    
    host = os.getenv("HOST")
    port = os.getenv("PORT")
    debug = os.getenv("DEBUG")
    mongo_url = os.getenv("MONGO_URL")
    api_prefix:str = os.getenv("APIPREFIX", "/api/v1")
  
@lru_cache
def cache_data():
    settings = Settings()
    return settings
    

# print(settings.api_prefix)
