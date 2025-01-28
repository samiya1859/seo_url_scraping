# SEO URL Scraping

This project provides functions to scrape metadata (title, meta description, Open Graph properties) and valid URLs (anchor and image URLs) from a given webpage. The scraper checks HTTP/HTTPS URLs, extracts relevant metadata from the page, and helps in SEO analysis.

## Features

- **Metadata Extraction**: Scrape the page's title, meta description, and Open Graph tags (`og:title` and `og:description`).
- **URL Scraping**: Extract all anchor (`<a>`) and image (`<img>`) URLs from the page, including relative URLs, and validate them as HTTP/HTTPS links.
- **URL Status Check**: Check the status code of the URLs to ensure they are reachable.

## Requirements

Before running the code, make sure to install the required dependencies listed in the `requirements.txt` file.

### Clone the project
```bash
git clone https://github.com/samiya1859/seo_url_scraping.git
```

### Navigate to the project directory
```bash
cd seo_url_scraping
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run the file
```bash
python data_scrape.py
```
## Functions
### Metadata Functions:
- fetch_meta_title(url)
Fetches the <title> content of the webpage at the given URL.

- fetch_meta_description(url)
Extracts the content of the <meta name="description"> tag of the webpage.

- fetch_og_title(url)
Retrieves the content of the <meta property="og:title"> tag for the Open Graph title.

- fetch_og_description(url)
Extracts the content of the <meta property="og:description"> tag for the Open Graph description.

### URL Scraping Functions:
- fetch_urls(url)
Scrapes all anchor (<a>) and image (<img>) URLs from the webpage at the given URL. It returns two lists: one for anchor URLs and another for image URLs, validating HTTP/HTTPS links.

- check_url_status(urls)
Takes a list of URLs and checks the HTTP status code for each. It returns a list of status messages indicating whether the URL is reachable or failed to load.
