import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_notification(name, price):
    message = f"🛒 **{name}** está abaixo do preço! Preço atual: R$ {price:.2f}"
    print(message)

    if not WEBHOOK_URL:
        print("Webhook do Discord não configurado.")
        return

    data = {"content": message}
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        response.raise_for_status()
        print("Notificação enviada para o Discord com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar notificação para o Discord: {e}")
