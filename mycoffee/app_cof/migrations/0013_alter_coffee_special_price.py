# Generated by Django 4.2.2 on 2023-09-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_cof", "0012_alter_coffee_special_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coffee",
            name="special_price",
            field=models.IntegerField(null=True),
        ),
    ]
