# Generated by Django 4.2.2 on 2023-09-20 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_cof", "0004_coffee_description"),
        ("app_gen", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="coffee",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app_cof.coffee",
            ),
        ),
    ]
