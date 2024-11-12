# Generated by Django 5.1.2 on 2024-11-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0019_alter_course_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="type",
            field=models.CharField(
                choices=[
                    ("basic_course", "basic course"),
                    ("elective_course", "elective course"),
                    ("specialy_course", "specialy course"),
                    ("public_course", "public course"),
                ],
                max_length=30,
            ),
        ),
    ]
