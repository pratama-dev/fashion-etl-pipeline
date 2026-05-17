import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time

logging.basicConfig(level=logging.INFO)

def scrape_page(page_number, session):
    """Fungsi untuk mengekstrak data dari satu halaman."""
    if(page_number == 1):
        url = f"https://fashion-studio.dicoding.dev"
    else:
        url = f"https://fashion-studio.dicoding.dev/page{page_number}"
    
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        cards = soup.find_all('div', class_='collection-card')
        for card in cards:
            title_elem = card.find('h3', class_='product-title')
            title = title_elem.text.strip() if title_elem else None

            price_elem = card.find(class_='price')
            price = price_elem.text.strip() if price_elem else None

            # Elemen rating, warna, ukuran, dan gender biasanya ada di dalam tag <p>
            details = card.find_all('p')
            rating = details[0].text.strip() if len(details) > 0 else None
            colors = details[1].text.strip() if len(details) > 1 else None
            size = details[2].text.strip() if len(details) > 2 else None
            gender = details[3].text.strip() if len(details) > 3 else None

            products.append({
                'Title': title,
                'Price': price,
                'Rating': rating,
                'Colors': colors,
                'Size': size,
                'Gender': gender
            })
        return products
    except requests.exceptions.RequestException as e:
        logging.error(f"Error extracting page {page_number}: {e}")
        return []

def extract_all(total_pages=50):
    """Fungsi utama untuk mengekstrak seluruh halaman."""
    
    all_data = []
    session = requests.Session()

    for i in range(1, total_pages + 1):
        logging.info(f"Scraping page {i}...")
        data = scrape_page(i, session)
        print(f"Page {i}: {len(data)} data")
        all_data.extend(data)
        time.sleep(1)

    return pd.DataFrame(all_data)