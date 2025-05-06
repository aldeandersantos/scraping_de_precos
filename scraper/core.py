import requests
from bs4 import BeautifulSoup

def scrape_price(url, selector, custom_headers=None):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        # Se tiver headers personalizados, use-os
        if custom_headers:
            headers.update(custom_headers)
            
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lança uma exceção para códigos de erro HTTP
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Se não tiver seletor, não conseguimos extrair o preço
        if not selector:
            print(f"Seletor não fornecido para URL: {url}")
            return None
            
        # Tenta encontrar o elemento com o preço
        price_element = soup.select_one(selector)
        
        # Verifica se o elemento foi encontrado
        if not price_element:
            print(f"Elemento de preço não encontrado usando o seletor: {selector}")
            return None
            
        # Extrai o texto do elemento
        price_text = price_element.text
        
        # Verifica se o texto foi extraído
        if not price_text:
            print("Texto de preço vazio")
            return None
            
        # Processa o texto do preço
        # Remove caracteres não numéricos e converte para float
        price_text = price_text.strip()
        # Assume formato brasileiro: R$ 1.999,90
        price_numeric = price_text.replace("R$", "").replace(".", "").replace(",", ".").strip()
        
        try:
            return float(price_numeric)
        except ValueError:
            print(f"Não foi possível converter o texto do preço para um número: '{price_text}'")
            return None
            
    except Exception as e:
        print(f"Erro ao fazer scraping: {e}")
        return None
