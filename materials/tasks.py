from datetime import datetime

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
# from django.utils.timezone import datetime

from config.settings import EMAIL_HOST_USER


# @shared_task
# def send_mail_about_course_updating(course_name, email):
#     subject = f'Обновление курса: {course_name}'
#     message = f'Курс "{course_name}" был обновлен.'
#     send_mail(subject, message, 'your_email@example.com', [email])
# # def send_mail_about_course_updating(email_list, course):
#     """Отправляет письмо об обновления курса пользователю."""
#
#     # Преобразование даты в удобный вид.
#     updated_at = datetime.strftime(timezone.now(), "%d.%m.%Y %H:%M")
#
#     # Создание текста письма и отправка его на адреса подписчиков.
#     message = f"Курc {course} обновлен {updated_at}."
#     send_mail("Обновление курса", message, EMAIL_HOST_USER, email_list)

  # def check_course_updates():
  #       updated_courses = Course.objects.filter(updated_at__gt=datetime.datetime.now() - datetime.timedelta(hours=1))
  #       for course in updated_courses:
  #           send_mail(
  #               subject='Курс обновлен!',
  #               message=f'Курс "{course.title}" был обновлен!',
  #               from_email=settings.EMAIL_HOST_USER,
  #               recipient_list=['your_email@example.com'],
  #           )