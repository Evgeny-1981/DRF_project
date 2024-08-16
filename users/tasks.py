from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_inactive_users():
    """
    Определяем дату 30 дней назад и получаем пользователей по полю is_active=True
    и поле last_login меньше thirty_days_ago
    """
    thirty_days_ago = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(
        is_active=True, last_login__lt=thirty_days_ago
    ).exclude(is_superuser=True)
    for user in inactive_users:
        user.is_active = False
        user.save()
    return f"Заблокировано {len(inactive_users)} пользователя."
