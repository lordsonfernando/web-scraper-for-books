import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    all_h3_tags = soup.find_all('h3')

    if all_h3_tags:
        print("Full names from <h3> tags:")
        for h3_tag in all_h3_tags:
            # Find the <a> tag within the <h3> tag
            link_tag = h3_tag.find('a')
            if link_tag and 'title' in link_tag.attrs:
                full_name = link_tag['title']
                print(full_name)
            elif link_tag and link_tag.get_text(strip=True):
                # Fallback: If no title attribute, try getting text from <a>
                full_name = link_tag.get_text(strip=True)
                print(full_name)
            else:
                # If no <a> or title, try getting text directly from <h3>
                full_name = h3_tag.get_text(strip=True)
                print(full_name)
    else:
        print("No <h3> tags found on the page.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
