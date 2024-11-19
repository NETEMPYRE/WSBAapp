# Generated by Django 5.1.3 on 2024-11-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlayerID', models.TextField()),
                ('PaymentMethod', models.TextField()),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
