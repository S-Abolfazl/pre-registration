# Generated by Django 5.1.2 on 2024-11-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0009_alter_course_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="type",
            field=models.CharField(
                choices=[
                    ("specialy_course", "specialy course"),
                    ("elective_course", "elective course"),
                    ("public_course", "public course"),
                    ("basic_course", "basic course"),
                ],
                max_length=30,
            ),
        ),
    ]
