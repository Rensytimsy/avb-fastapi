from beanie import init_beanie, Document

class Users(Document):
    name:str
    age:int
    department: str
    
    class Settings: 
        name = "Users"
        
class UrlRedirect(Document):
    original_url: str
    short_url: str
    
    class Settings:
        name = "Short Urls"



    