# Generated by Django 4.2.7 on 2024-04-25 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customusermodel",
            name="phone_number",
            field=models.CharField(
                blank=True,
                help_text='Введіть номер телефону у форматі "+32xxxxxxxxx"',
                max_length=15,
                null=True,
                verbose_name="Номер телефону",
            ),
        ),
    ]