# Generated by Django 5.0.7 on 2024-08-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0005_alter_lesson_link_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="link_video",
            field=models.URLField(
                blank=True, max_length=250, null=True, verbose_name="Ссылка на видео"
            ),
        ),
    ]