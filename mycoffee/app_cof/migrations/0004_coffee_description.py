# Generated by Django 4.2.2 on 2023-09-20 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_cof", "0003_remove_coffee_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="coffee", name="description", field=models.TextField(null=True),
        ),
    ]
