# Generated by Django 4.2.2 on 2023-09-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_gen", "0004_remove_subscription_coffee_subscription_coffee_set"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="registerd_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
