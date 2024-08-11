# Generated by Django 5.0.7 on 2024-08-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0013_alter_course_amount_alter_lesson_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="amount",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="amount",
        ),
        migrations.AddField(
            model_name="course",
            name="price_usd",
            field=models.PositiveIntegerField(
                blank=True, default=0, null=True, verbose_name="Стоимость курса, usd"
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="price_usd",
            field=models.PositiveIntegerField(
                blank=True, default=0, null=True, verbose_name="Стоимость урока, usd"
            ),
        ),
    ]
