# Generated by Django 5.1.2 on 2024-11-30 16:17

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllCourses",
            fields=[
                (
                    "course_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("courseName", models.CharField(max_length=255, unique=True)),
                ("unit", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("elective_course", "elective course"),
                            ("practical_course", "practical course"),
                            ("theory_course", "theory course"),
                            ("basic_course", "basic course"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
            options={
                "db_table": "AllCourses",
            },
        ),
        migrations.CreateModel(
            name="Rule",
            fields=[
                (
                    "rule_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("entry_rule", "entry_rule")], max_length=30
                    ),
                ),
                ("values", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "Rule",
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "c_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("teacherName", models.CharField(max_length=255)),
                ("isExperimental", models.BooleanField()),
                ("dateTime", models.DateTimeField(auto_now_add=True)),
                ("exam_dateTime", models.DateTimeField()),
                ("capacity", models.IntegerField()),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.allcourses",
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
                        to="course.allcourses",
                    ),
                ),
                (
                    "prereq_course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="is_prereq_of",
                        to="course.allcourses",
                    ),
                ),
            ],
            options={
                "db_table": "Prereq",
                "unique_together": {("course", "prereq_course")},
            },
        ),
        migrations.CreateModel(
            name="CourseRule",
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
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
                (
                    "rule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.rule"
                    ),
                ),
            ],
            options={
                "db_table": "CourseRule",
                "unique_together": {("course", "rule")},
            },
        ),
    ]
