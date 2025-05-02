import json
import time
from scraper.core import scrape_price
from notifier.core import send_notification

PRODUCTS_FILE = "data/products.json"

def main():
    with open(PRODUCTS_FILE, "r", encoding="utf-8") as f:
        products = json.load(f)

    for product in products:
        print(f"Verificando: {product['name']}")
        price = scrape_price(product['url'], product['selector'])

        if price is None:
            print(f"Preço não encontrado para {product['name']}\n")
            continue

        if price <= product['threshold']:
            send_notification(product['name'], price)
        else:
            print(f"{product['name']}: R$ {price} está acima do limite R$ {product['threshold']}\n")

        time.sleep(2)  # pequeno delay para evitar bloqueios

if __name__ == '__main__':
    main()
