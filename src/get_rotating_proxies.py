import requests
from bs4 import BeautifulSoup as bs 
import random 
import traceback

def get_free_proxies():
    url = "https://free-proxy-list.net"

    # request and grab content 
    soup = bs(requests.get(url).content, 'html.parser')

    # a list to store proxies
    proxies = []

    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try: 
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue

    return proxies

print(get_free_proxies())

## RUN THE CODE ABOVE BEFORE GOING FORWARD 

# Test the proxies with google.com
all_us_proxies = [] # contains all the proxies from United States 

def get_working_proxies():
    # working_proxies = []

    for proxy in all_us_proxies:
        print(f"Using proxy: {proxy}")
        try:
            r = requests.get("https://www.google.com",
                             proxies=proxy, 
                             timeout=3)
            print(r.status_code)

        except:
            pass

