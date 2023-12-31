# Generated by Django 4.2.3 on 2023-07-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="OtpCode",
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
                ("phone_number", models.CharField(max_length=11)),
                ("code", models.SmallIntegerField()),
                ("created", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
