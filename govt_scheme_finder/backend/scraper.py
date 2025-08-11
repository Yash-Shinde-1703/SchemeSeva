import requests
from bs4 import BeautifulSoup
import json
import time
import os

WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/List_of_schemes_of_the_government_of_India"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
OUTPUT_DIR = "/app/govt_scheme_finder/backend/"

def get_soup(url, retries=3, delay=5):
    for i in range(retries):
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.exceptions.RequestException as e:
            print("Error fetching " + url + ": " + str(e) + ". Retrying in " + str(delay) + " seconds...")
            time.sleep(delay)
    print("Failed to fetch " + url + " after " + str(retries) + " retries.")
    return None

def scrape_schemes():
    soup = get_soup(WIKIPEDIA_URL)
    if not soup:
        return [], []

    schemes = []
    categories = set()

    # Find the main table of schemes
    table = soup.find("table", class_="wikitable")
    if table:
        rows = table.find_all("tr")[2:]  # Skip the header rows
        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 6:
                scheme_name = cols[0].text.strip()
                cs_css = cols[1].text.strip()
                lead_ministry = cols[2].text.strip()
                year = cols[3].text.strip()
                sector = cols[4].text.strip()
                summary = cols[5].text.strip()

                schemes.append({
                    "name": scheme_name,
                    "type": cs_css,
                    "ministry": lead_ministry,
                    "year": year,
                    "category": sector,
                    "summary": summary,
                    "state": "Central" # Assume central for the main table
                })
                categories.add(sector)

    # Scrape state-sponsored schemes
    state_sections = soup.find_all("span", class_="mw-headline")
    for section in state_sections:
        state_name = section.get_text(strip=True)
        # Check if it's a state section
        if state_name in ["Karnataka", "Madhya Pradesh", "Maharashtra", "Telangana", "Odisha", "Tamil Nadu", "West Bengal", "Uttar Pradesh"]:
            ul = section.find_next("ul")
            if ul:
                for li in ul.find_all("li"):
                    schemes.append({
                        "name": li.text.strip(),
                        "type": "State Sponsored",
                        "ministry": "",
                        "year": "",
                        "category": "State Specific",
                        "summary": "",
                        "state": state_name
                    })
                    categories.add("State Specific")

    return schemes, list(categories)


if __name__ == "__main__":
    schemes, categories = scrape_schemes()

    schemes_path = os.path.join(OUTPUT_DIR, "schemes.json")
    with open(schemes_path, "w") as f:
        json.dump(schemes, f, indent=4)

    categories_path = os.path.join(OUTPUT_DIR, "categories.json")
    with open(categories_path, "w") as f:
        json.dump(categories, f, indent=4)

    print("Scraping complete. Found " + str(len(schemes)) + " schemes and " + str(len(categories)) + " categories.")
