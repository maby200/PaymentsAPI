# Generated by Django 4.1.4 on 2022-12-29 23:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment_user', '0006_alter_payments_expiration_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentsV2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('amount', models.FloatField(default=0.0)),
                ('expiration_date', models.DateField(default=datetime.date(2023, 1, 1))),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_v2', to='services.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_v2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
