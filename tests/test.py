"""
I am using this file to perform searches
"""

# Load the relevant libraries 
import requests
from fake_useragent import UserAgent
# from bs4 import BeautifulSoup
# import time
# import logging  # will be used later

# Retrieve the hmtl content 
url = "https://www.docinfo.org/"
headers = {
    "User-Agent": UserAgent.random
    }
response = requests.get(url) #, headers=headers)

print(response.text)