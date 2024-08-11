import requests
import stripe
from rest_framework import status

from config.settings import STRIPE_SECRET_KEY, CUR_API_KEY, CUR_API_URL

stripe.api_key = STRIPE_SECRET_KEY


def choose_material(payment):
    """Функция для выбора продукта для оплаты"""

    if payment.paid_lesson:
        return payment.paid_lesson
    elif payment.paid_course:
        return payment.paid_course
    else:
        raise ValueError("Необходимо выбрать курс или урок для оплаты")


def convert_usd_to_rub(price_usd):
    """Функция конвертирует usd в rub"""

    price_rub = 0
    response = requests.get(
        f"{CUR_API_URL}v3/latest?apikey={CUR_API_KEY}&currencies=RUB"
    )
    if response.status_code == status.HTTP_200_OK:
        exchange_rate = response.json()["data"]["RUB"]["value"]
        price_rub = int(price_usd * exchange_rate)
    return price_rub


def create_stripe_product(material):
    """Создает продукт в страйпе."""

    return stripe.Product.create(name=f"Оплата за курс(урок) - {material}")


def create_stripe_price(price, product):
    """Создает цену в страйпе."""
    price_rub = convert_usd_to_rub(price)
    return stripe.Price.create(
        currency="rub",
        unit_amount=price_rub * 100,
        product=product,
    )


def create_stripe_session(price, payment_pk):
    """Создает сессию оплаты в страйпе."""

    session = stripe.checkout.Session.create(
        success_url=f"http://127.0.0.1:8000/payment/success/{payment_pk}",
        line_items=[{"price": price, "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


def retrieve_sessions_statuses(session_id):
    """Получение статуса сессии в страйпе."""

    info = stripe.checkout.Session.retrieve(session_id)
    return info.get("payment_status")
