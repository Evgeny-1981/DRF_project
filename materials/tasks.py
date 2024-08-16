from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from materials.models import Subscription, Course


@shared_task
def send_mail_about_course_updating(course_id):
    course = Course.objects.get(pk=course_id)
    print(course)
    course_users = Subscription.objects.filter(course=course_id)
    print(course_users)

    email_list = []
    for user in course_users:
        email_list.append(user.USERNAME_FIELD)
        print(email_list)
    # if email_list:
    #     send_mail(
    #         subject=f"Обновление по курсу {course.name}",
    #         message=f"Вы подписаны на обновления курса, вышла новая информация по курсу.",
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=email_list,
    #         fail_silently=True
    #     )
