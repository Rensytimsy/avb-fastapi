import hashlib

class UrlShortener:
    def __init__(self):
        self.dynamic_url = {}
        self.url_prefix = "http://localhost:7000/api/v1/simple-url"
    
    def shorten_url(self, original_url: str):
        hash_url = hashlib.md5(original_url.encode()).hexdigest()[:9]
        short_url = f"{self.url_prefix}/{hash_url}"
        self.dynamic_url[short_url] = original_url
        return short_url

shorten_url = UrlShortener()
