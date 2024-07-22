from django.db import models

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(max_length=120, verbose_name="наименование курса")
    slug = models.CharField(max_length=120, verbose_name="имя слаг", unique=True)
    description = models.TextField(verbose_name="описание курса", **NULLABLE)
    image = models.ImageField(
        upload_to="media/course_image/", verbose_name="изображение", **NULLABLE
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
    slug = models.CharField(max_length=120, verbose_name="имя слаг", unique=True)
    description = models.TextField(verbose_name="описание урока", **NULLABLE)
    image = models.ImageField(upload_to="media/lesson_image/", verbose_name="изображение", **NULLABLE)
    link_video = models.FileField(upload_to="media/lesson_video", verbose_name="видео", **NULLABLE)
    name_course = models.ForeignKey(Course, verbose_name="название курса", related_name="урок", on_delete=models.CASCADE,
                                    **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "lesson"
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("name", )