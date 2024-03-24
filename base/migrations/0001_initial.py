# Generated by Django 4.0 on 2024-03-24 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('city_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=11)),
            ],
        ),
    ]