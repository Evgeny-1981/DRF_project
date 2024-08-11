# import requests
# from config.settings import CUR_API_URL, CUR_API_KEY
# from rest_framework import status
#
#
# def convert_usd_to_rub(price_usd):
#     """Функция конвертирует рубли в доллары"""
#     price_rub = 0
#     response = requests.get(f'{CUR_API_URL}v3/latest?apikey={CUR_API_KEY}&currencies=RUB')
#     if response.status_code == status.HTTP_200_OK:
#         exchange_rate = response.json()['data']['RUB']['value']
#         price_rub = int(price_usd * exchange_rate)
#     return price_rub
