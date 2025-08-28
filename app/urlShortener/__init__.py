"""
A simple url shortener module
Simply provide an url and you will get back the shortened url
"""
__version__ = "1.0.0"

from .shorten import shorten_url

__all__ = ["shorten_url"]
