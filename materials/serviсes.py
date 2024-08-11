import requests
from config.settings import CUR_API_URL, CUR_API_KEY
from rest_framework import status


def convert_rub_to_usd(rub_price):
    """Функция конвертирует рубли в доллары"""
    usd_price = 0
    response = requests.get(f'{CUR_API_URL}v3/latest?apikey={CUR_API_KEY}&currencies=RUB')
    if response.status_code == status.HTTP_200_OK:
        usd_rate = response.json()['data']['RUB']['value']
        usd_price = int(rub_price * usd_rate)
    return usd_price
