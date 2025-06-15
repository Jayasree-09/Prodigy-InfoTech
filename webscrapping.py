import requests
from bs4 import BeautifulSoup
import csv

# Target website
URL = "http://books.toscrape.com/"
response = requests.get(URL)

# Parse the page
soup = BeautifulSoup(response.text, 'html.parser')

# Open CSV file to write
with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating"])

    # Loop through each product
    for book in soup.find_all('article', class_='product_pod'):
        # Title
        title = book.h3.a['title']

        # Price
        price = book.find('p', class_='price_color').text.strip()

        # Rating (convert class to star rating text)
        rating_class = book.p['class'][1]
        rating_map = {
            "One": "1",
            "Two": "2",
            "Three": "3",
            "Four": "4",
            "Five": "5"
        }
        rating = rating_map.get(rating_class, "No Rating")

        # Write to CSV
        writer.writerow([title, price, rating])

print("Scraping complete! Data saved to 'books.csv'.")
