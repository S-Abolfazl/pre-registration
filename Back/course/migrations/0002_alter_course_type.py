# Generated by Django 5.1.2 on 2024-11-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="type",
            field=models.CharField(
                choices=[
                    ("specialy_course", "specialy course"),
                    ("basic_course", "basic course"),
                    ("public_course", "public course"),
                    ("elective_course", "elective course"),
                ],
                max_length=30,
            ),
        ),
    ]
