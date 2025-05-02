import requests
from bs4 import BeautifulSoup

def scrape_price(url, selector):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.select_one(selector)

        if element:
            price_text = element.get_text(strip=True)
            return extract_float_from_text(price_text)
        else:
            print("Seletor não encontrou o elemento.")
            return None
    except Exception as e:
        print(f"Erro ao fazer scraping: {e}")
        return None

def extract_float_from_text(text):
    import re
    numbers = re.findall(r'\d+[\.,]?\d*', text.replace('.', '').replace(',', '.'))
    if numbers:
        return float(numbers[0])
    return None
