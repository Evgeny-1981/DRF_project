# Generated by Django 5.0.7 on 2024-08-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0011_alter_course_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="amount",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Стоимость урока, руб"
            ),
        ),
    ]
