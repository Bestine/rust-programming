"""
The main script that will run doctors webscraping workflow
"""

import requests
from bs4 import BeautifulSoup
from gather_proxies import GatherProxies
import random
import time
from requests_html import HTMLSession
from playwright.sync_api import sync_playwright


# Test the proxies on the docs info website
url_doc = "https://www.docinfo.org/"
verified_proxies_US = GatherProxies()
# print(verified_proxies_US)

print(f"\n...GATHERING PROXIES COMPLETE! - {len(verified_proxies_US)} proxies verified!!!")

# session = HTMLSession()

# for proxy in verified_proxies_US:
#     print("Checking on site....")
#     time.sleep(random.randint(3, 9))
#     response = session.get(url_doc,
#                      proxies=proxy,
#                      timeout=3)
#     print(response.status_code)
#     print(response.text)

def scrape_with_playwright(current_proxy):
    with sync_playwright() as p:
        # Proxy details 
        proxy_details = current_proxy

        # launch browser with proxy settings
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(proxy = proxy_details, ignore_https_errors=True)
        page = context.new_page()
        
        # navigate to the page 
        page.goto("https://www.docinfo.org/", wait_until="networkidle", timeout=6000)

        time.sleep(5)

# Option 2
def scrape_with_js(current_proxy): # Ensure the proxy is `http`` not `server`
    # Start an HTML session
    session = HTMLSession()

    # Use rotating headers
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
    }
    response = session.get("https://docinfo.org", proxies=current_proxy, headers=headers)

    
    # # Fetch the page with proxy
    # response = session.get("https://docinfo.org", proxies=current_proxy)
     
    # Render JavaScript content
    response.html.render(timeout=20)  # Increase timeout if necessary

    # Get the response 
    print(response.status_code)

    # Close the session
    session.close()
        

for current_proxy in verified_proxies_US:
    print("Checking on site....")
    time.sleep(random.randint(3, 9))
    scrape_with_js(current_proxy)

    print("!!!CHECKING DONE!")
    