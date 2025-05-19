import unittest
import requests
from bs4 import BeautifulSoup

# Assuming the code you provided is in a file named 'scraper.py'
# If it's not, adjust the import accordingly.
import scraper

class TestScraper(unittest.TestCase):

    def test_successful_request(self):
        response = requests.get(scraper.url)
        self.assertEqual(response.status_code, 200)

    def test_h3_tags_exist(self):
        response = requests.get(scraper.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        h3_tags = soup.find_all('h3')
        self.assertGreater(len(h3_tags), 0, "No <h3> tags found on the page.")

    def test_full_names_extracted(self):
        response = requests.get(scraper.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        h3_tags = soup.find_all('h3')
        extracted_names = []
        for h3_tag in h3_tags:
            link_tag = h3_tag.find('a')
            if link_tag and 'title' in link_tag.attrs:
                extracted_names.append(link_tag['title'])
            elif link_tag and link_tag.get_text(strip=True):
                extracted_names.append(link_tag.get_text(strip=True))
            else:
                extracted_names.append(h3_tag.get_text(strip=True))

        # Check if at least some names were extracted (adjust the number if needed)
        self.assertGreater(len(extracted_names), 0, "No book names were extracted.")

        # You could add more specific tests here if you know expected book titles
        # For example:
        # self.assertIn("A Light in the Attic", extracted_names)
        # self.assertIn("Tipping the Velvet", extracted_names)

if __name__ == '__main__':
    unittest.main()
