# Generated by Django 4.2 on 2023-05-10 19:55

import college.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("college", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsLetter",
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
                ("name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=254)),
                ("course", models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name="college",
            name="image",
            field=models.ImageField(
                null=True, upload_to=college.models.College.img_path
            ),
        ),
        migrations.CreateModel(
            name="USNews",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TimesofIndia",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="QS",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Outlook",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NIRF",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MBAUniverse",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IndiaToday",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IndianExpress",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IndiaEducation",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IIRF",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EconomicTimes",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CollegeWorld",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BusinessToday",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ARIIA",
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
                ("year", models.IntegerField()),
                ("rank", models.IntegerField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Overall", "Overall"),
                            ("Engineering", "Engineering"),
                            ("Pharmacy", "Pharmacy"),
                            ("Management", "Management"),
                        ],
                        default="Overall",
                        max_length=250,
                    ),
                ),
                (
                    "college",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="college.college",
                    ),
                ),
            ],
        ),
    ]