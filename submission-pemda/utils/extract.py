import requests
from bs4 import BeautifulSoup
import time

def extract_data(base_url="https://fashion-studio.dicoding.dev"):
    all_products = []
    try:
        for page in range(1, 51):
            url = base_url if page == 1 else f"{base_url}/?page={page}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            cards = soup.find_all('div', class_='collection-card')
            
            for card in cards:
                try:
                    title_elem = card.find('h3', class_='product-title')
                    price_elem = card.find(class_='price')
                    p_elems = card.find_all('p')
                    rating_elem = p_elems[0] if len(p_elems) > 0 else None
                    colors_elem = p_elems[1] if len(p_elems) > 1 else None
                    size_elem = p_elems[2] if len(p_elems) > 2 else None
                    gender_elem = p_elems[3] if len(p_elems) > 3 else None

                    product = {
                        'Title': title_elem.text.strip() if title_elem else None,
                        'Price': price_elem.text.strip() if price_elem else None,
                        'Rating': rating_elem.text.replace('Rating: ', '').strip() if rating_elem else None,
                        'Colors': colors_elem.text.strip() if colors_elem else None,
                        'Size': size_elem.text.strip() if size_elem else None,
                        'Gender': gender_elem.text.strip() if gender_elem else None
                    }
                    all_products.append(product)
                except Exception:
                    continue
            time.sleep(1)
        return all_products
    except Exception as e:
        print(e)
        return None
