# Generated by Django 5.0.7 on 2024-08-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0014_remove_course_amount_remove_lesson_amount_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="updated_course",
            field=models.DateTimeField(
                auto_now=True, null=True, verbose_name="Дата обновления курса"
            ),
        ),
    ]
