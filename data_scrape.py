from utils.generate_location import generate_location
from utils.seo_element_fetching import fetch_meta_title, fetch_meta_description,fetch_og_title,fetch_og_description
from utils.status_checking import fetch_anchor_tags,check_url_status

# Test the location generation
if __name__ == "__main__":
    country, city = generate_location()
    base_url = f'https://www.rentbyowner.com/all/{country}/{city}'

    print(f"Generated URL: {base_url}")

    # Fetch and print the meta title
    meta_title = fetch_meta_title(base_url)
    print(f"Meta Title: {meta_title}")

    # Fetch and print the meta description
    meta_description = fetch_meta_description(base_url)
    print(f"Meta Description: {meta_description}")

    # Fetch and print the Open Graph title
    og_title = fetch_og_title(base_url)
    print(f"Open Graph Title: {og_title}")

    # Fetch and print the Open Graph description
    og_description = fetch_og_description(base_url)
    print(f"Open Graph Description: {og_description}")

     # Fetch and print all anchor tags (URLs)
    anchor_urls = fetch_anchor_tags(base_url)
    print(f"Found {len(anchor_urls)} anchor tags.")
    
    # Check status for each URL and print the result
    url_status = check_url_status(anchor_urls)
    for status in url_status:
        print(status)
