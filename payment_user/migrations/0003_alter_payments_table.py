# Generated by Django 4.1.4 on 2022-12-28 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_user', '0002_alter_payments_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='payments',
            table='Payment',
        ),
    ]
