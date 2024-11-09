import requests
from bs4 import BeautifulSoup
import pandas as pd

def GatherProxies():
    # URL of the website
    url = 'https://free-proxy-list.net/'
    verified_proxies = []

    # Send a GET request to the URL
    response = requests.get(url)
    # print(response.text)
    ip_address = []
    port = []
    country = []
    https_secured = []

    # Parse the html 
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    table_bodies = table.find('tbody')
    for tr in table_bodies:
        td_s = tr.find_all('td')
        
        # extract all the information
        ip_address.append(td_s[0].text)
        port.append(td_s[1].text)
        country.append(td_s[3].text)
        https_secured.append(td_s[6].text)

    # Create a data frame 
    proxies_df = pd.DataFrame({
        'ip_address': ip_address,
        'port': port,
        'country':country,
        'https_secured': https_secured
    })

    # Filter US secured proxies 
    US_proxies_df = proxies_df[(proxies_df["country"]=="United States")&\
        (proxies_df["https_secured"]=="yes")].reset_index(drop=True)

    # Verify the proxies and extract the working ones 
    print(f"VERIFYING {US_proxies_df.shape[0]} PROXIES ...\n")

    for i_proxy in range(US_proxies_df.shape[0]):
        current_ip_address = US_proxies_df['ip_address'][i_proxy]
        current_port = US_proxies_df['port'][i_proxy]

        # print(f"On proxy: {current_ip_address}")
        
        current_proxy = {
            'http':f'http://{current_ip_address}:{current_port}'
            }

        try:
            r = requests.get("https://www.google.com/",
                                proxies=current_proxy, 
                                timeout=3)
            if r.status_code==200:
                verified_proxies.append(current_proxy)
                # print("Proxy verified!!!")
            else:
                pass

        except:
            # print("COULD NOT WORK!!!")
            pass

    return verified_proxies

# Gather the proxies 
# GatherProxies()