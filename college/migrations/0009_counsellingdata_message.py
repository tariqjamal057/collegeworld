# Generated by Django 4.2 on 2023-05-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("college", "0008_alter_counsellingdata_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="counsellingdata",
            name="message",
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
