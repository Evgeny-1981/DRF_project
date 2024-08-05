# Generated by Django 5.0.7 on 2024-07-25 02:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_alter_lesson_name_course"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="paid_lesson",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payment",
                to="materials.lesson",
                verbose_name="урок",
            ),
        ),
    ]
