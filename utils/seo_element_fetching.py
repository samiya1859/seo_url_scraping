import requests
from bs4 import BeautifulSoup # type: ignore

def fetch_meta_title(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the <title> tag content
        title = soup.title.string if soup.title else 'No title found'
        return title
    else:
        return f"Failed to retrieve page, status code: {response.status_code}"

def fetch_meta_description(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the meta description content
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description and 'content' in meta_description.attrs:
            return meta_description.attrs['content']
        else:
            return 'No meta description found'
    else:
        return f"Failed to retrieve page, status code: {response.status_code}"
    
def fetch_og_title(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the og:title content
        og_title = soup.find('meta', attrs={'property': 'og:title'})
        if og_title and 'content' in og_title.attrs:
            return og_title.attrs['content']
        else:
            return 'No Open Graph title found'
    else:
        return f"Failed to retrieve page, status code: {response.status_code}"
    
def fetch_og_description(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the og:description content
        og_description = soup.find('meta', attrs={'property': 'og:description'})
        if og_description and 'content' in og_description.attrs:
            return og_description.attrs['content']
        else:
            return 'No Open Graph description found'
    else:
        return f"Failed to retrieve page, status code: {response.status_code}"