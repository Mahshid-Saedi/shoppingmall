# Generated by Django 4.2.3 on 2023-08-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="products/%Y/%m/%d/"),
        ),
    ]
