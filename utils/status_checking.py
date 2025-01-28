import requests
from bs4 import BeautifulSoup  # type: ignore
from urllib.parse import urlparse, urljoin


def fetch_anchor_urls(soup, base_url):
    """
    Fetch and process all anchor URLs from the BeautifulSoup object.

    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object containing the parsed HTML.
        base_url (str): The base URL used for resolving relative URLs.

    Returns:
        list: A list of valid anchor URLs.
    """
    anchor_urls = []
    anchors = soup.find_all("a", href=True)
    for anchor in anchors:
        href = anchor["href"]
        parsed_href = urlparse(href)

        if parsed_href.scheme in ["http", "https"]:
            anchor_urls.append(href)
        elif parsed_href.scheme == "":
            # Handle relative URLs by joining them with the base URL
            full_url = urljoin(base_url, href)
            parsed_full_url = urlparse(full_url)
            if parsed_full_url.scheme in ["http", "https"]:
                anchor_urls.append(full_url)

    # Remove duplicates
    return list(set(anchor_urls))


def fetch_image_urls(soup):
    """
    Fetch and process all image URLs from the BeautifulSoup object.

    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object containing the parsed HTML.

    Returns:
        list: A list of valid image URLs.
    """
    image_urls = []
    images = soup.find_all("img", src=True)
    for img in images:
        src = img["src"]
        if src.startswith("http://") or src.startswith("https://"):
            image_urls.append(src)

    # Remove duplicates
    return list(set(image_urls))


def fetch_urls(url):
    """
    Fetches all anchor and image URLs from the given URL.

    Parameters:
        url (str): The URL of the webpage to scrape.

    Returns:
        tuple: A tuple containing two lists - valid anchor URLs and valid image URLs (duplicates removed).
    """
    response = requests.get(url)
    if response.status_code != 200:
        return f"Failed to retrieve page, status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Fetch valid anchor URLs
    anchor_urls = fetch_anchor_urls(soup, url)
    total_anchors = len(soup.find_all("a", href=True))
    valid_http_anchor_urls = len(anchor_urls)

    # Fetch valid image URLs
    image_urls = fetch_image_urls(soup)
    total_images = len(soup.find_all("img", src=True))
    valid_http_image_urls = len(image_urls)

    print(f"Total anchor tags found: {total_anchors}")
    print(
        f"Anchor tags with valid 'http/https' URLs: {valid_http_anchor_urls} (After removing duplicates)"
    )
    print(f"Total image tags found: {total_images}")
    print(
        f"Image tags with valid 'http/https' URLs: {valid_http_image_urls} (After removing duplicates)"
    )

    return anchor_urls, image_urls


def check_url_status(urls):
    """
    Check the HTTP status codes of a list of URLs.

    Args:
        urls (list): A list of URLs to check.

    Returns:
        list: A list of strings, each containing the URL and its corresponding HTTP status code
              or an error message if the URL failed to load.
    """
    url_status = []
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                url_status.append(f"URL: {url}, status: 200")
            else:
                url_status.append(f"URL: {url}, status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            url_status.append(f"URL: {url} failed to load, error: {e}")

    return url_status
