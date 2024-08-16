from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from materials.models import Subscription, Course


@shared_task
def send_mail_about_course_updating(course_id):
    """Отправляем письма об обновлении курса подписчикам курса"""
    course = Course.objects.get(pk=course_id)
    subscription_info = Subscription.objects.filter(course=course_id)

    email_list = []
    for subscription in subscription_info:
        email_list.append(subscription.user.email)
    if email_list:
        send_mail(
            subject=f"Обновление по курсу {course.name}",
            message=f"Вы подписаны на обновления курса, вышла новая информация по курсу."
            f"Вот, что изменилось: {course.description}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_list,
            fail_silently=True,
        )
