# Page Scraper - Create an application which connects to a site and pulls out all links, or images, and saves them to a list. 
# Optional: Organize the indexed content and don’t allow duplicates. Have it put the results into an easily searchable index file.

import requests
from bs4 import BeautifulSoup


def accessLink(url: str) -> str:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.text
    elif response.status_code == 404:
        raise requests.exceptions.RequestException("404 Not Found")
    
def parseResponse(response: str) -> str:
    soup = BeautifulSoup(response, 'html.parser')
    images = soup.find_all('img')
    links = soup.find_all('a')
    linkArray = []
    imageArray = []
    for link in links:
        linkArray.append(link.get("href"))
        
    for image in images:
        imageArray.append(image.get("href"))
        
    return linkArray, imageArray

if __name__ == "__main__":
    response = None
    links = []
    images = []
    
    try:
        response = accessLink("https://www.bbc.co.uk/news")
    except requests.Timeout:
        print("Error: Client timeout")
        exit()
    except requests.exceptions.RequestException as err:
        print("Error: ", err)
        exit()
    
    links, images = parseResponse(response)

        
    
        
        
    