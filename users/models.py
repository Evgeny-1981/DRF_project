from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=30, verbose_name='Контактный телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Автар', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='Страна', **NULLABLE)
    token = models.CharField(max_length=100, verbose_name='Токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)


class Payment(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    data_payment = models.DateTimeField(auto_now_add=True, verbose_name='дата платежа')
    paid_course = models.ForeignKey(Course, verbose_name='курс', on_delete=models.CASCADE, **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, verbose_name='урок', on_delete=models.CASCADE, **NULLABLE)
    summ_payment = models.FloatField(verbose_name='сумма платежа')
    payment_method = models.CharField(max_length=255, verbose_name='способ платежа')

    def __str__(self):
        return (f"Студент: {self.user} оплатил: {self.paid_course if self.paid_course else self.paid_lesson}, "
                f"сумма: {self.summ_payment}, способ платежа: {self.payment_method}")

    class Meta:
        db_table = "payment"
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ("user", )
