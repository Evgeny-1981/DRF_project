from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(max_length=120, verbose_name="наименование курса")
    description = models.TextField(verbose_name="описание курса", **NULLABLE)
    image = models.ImageField(
        upload_to="media/course_image/", verbose_name="изображение", **NULLABLE
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="автор курса",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "course"
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ("name",)


class Lesson(models.Model):
    name = models.CharField(max_length=120, verbose_name="наименование урока")
    description = models.TextField(verbose_name="описание урока", **NULLABLE)
    image = models.ImageField(
        upload_to="media/lesson_image/", verbose_name="изображение", **NULLABLE
    )
    link_video = models.URLField(max_length=250,
                                 verbose_name="Ссылка на видео", **NULLABLE
                                 )
    name_course = models.ForeignKey(
        Course,
        related_name="lesson",
        verbose_name="название курса",
        on_delete=models.CASCADE,
        **NULLABLE,
    )
    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="автор урока",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "lesson"
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("name",)


class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name="Пользователь", **NULLABLE, )
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name="Подписка на курс", **NULLABLE, )

    def __str__(self):
        return f"Пользователь {self.user}, подписан на курс: {self.course}"

    class Meta:
        db_table = "subscription"
        verbose_name = "Подписку"
        verbose_name_plural = "Подиписки"
        ordering = ("user",)
