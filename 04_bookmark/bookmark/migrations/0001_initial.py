# Generated by Django 4.1.3 on 2022-11-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bookmark",
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
                ("site_name", models.CharField(max_length=100)),
                ("url", models.URLField(verbose_name="Site URL")),
            ],
        ),
    ]
