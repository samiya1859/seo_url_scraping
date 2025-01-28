from utils.generate_location import generate_location
from utils.seo_element_fetching import (
    fetch_meta_title,
    fetch_meta_description,
    fetch_og_title,
    fetch_og_description,
)
from utils.status_checking import fetch_urls, check_url_status

def main():
    """
    Main function to test location generation and scrape meta elements, URLs, and statuses
    for the generated URL.
    """
    # Generate a random location (country and city)
    country, city = generate_location()
    base_url = f"https://www.rentbyowner.com/all/{country}/{city}"

    print(f"Generated URL: {base_url}\n")

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

    # Fetch and print all anchor tags and image tags (URLs)
    anchor_urls, image_urls = fetch_urls(base_url)

  

    # Optionally, check the status of all valid URLs (anchor and image)
    all_urls = anchor_urls + image_urls
    url_status = check_url_status(all_urls)
    print("\nURL Status Check Results:")
    for status in url_status:
        print(status)


if __name__ == "__main__":
    main()
