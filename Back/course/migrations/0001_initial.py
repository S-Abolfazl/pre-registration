# Generated by Django 5.1.2 on 2024-11-27 16:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("course_id", models.CharField(max_length=255)),
                ("courseName", models.CharField(max_length=255)),
                ("teacherName", models.CharField(max_length=255)),
                ("isExperimental", models.BooleanField()),
                ("dateTime", models.DateTimeField(auto_now_add=True)),
                ("exam_dateTime", models.DateTimeField()),
                ("capacity", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("specialy_course", "specialy course"),
                            ("public_course", "public course"),
                            ("elective_course", "elective course"),
                            ("basic_course", "basic course"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
            options={
                "db_table": "Course",
            },
        ),
        migrations.CreateModel(
            name="Prereq",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prereqs_for",
                        to="course.course",
                    ),
                ),
                (
                    "prereq_course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="is_prereq_of",
                        to="course.course",
                    ),
                ),
            ],
            options={
                "db_table": "Prereq",
                "unique_together": {("course", "prereq_course")},
            },
        ),
    ]
