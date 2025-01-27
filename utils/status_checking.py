import requests
from bs4 import BeautifulSoup

def fetch_anchor_tags(url):
    response = requests.get(url)
    anchor_urls = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all anchor tags with href attribute
        anchors = soup.find_all('a', href=True)
        for anchor in anchors:
            anchor_urls.append(anchor['href'])
    else:
        return f"Failed to retrieve page, status code: {response.status_code}"
    
    return anchor_urls

def check_url_status(urls):
    url_status = []
    for url in urls:
        try:
            # Make GET request to check status
            response = requests.get(url)
            if response.status_code == 200:
                url_status.append(f"URL: {url}, status: 200")
            else:
                url_status.append(f"URL: {url}, status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            url_status.append(f"URL: {url} failed to load, error: {e}")
    
    return url_status