# Generated by Django 4.2.2 on 2023-09-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_cof", "0004_coffee_description"),
        ("app_gen", "0003_alter_subscription_coffee"),
    ]

    operations = [
        migrations.RemoveField(model_name="subscription", name="coffee",),
        migrations.AddField(
            model_name="subscription",
            name="coffee_set",
            field=models.ManyToManyField(to="app_cof.coffee"),
        ),
    ]
