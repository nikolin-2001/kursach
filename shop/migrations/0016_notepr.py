# Generated by Django 3.2.9 on 2021-11-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20211111_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notepr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo', models.CharField(max_length=200, verbose_name='Скдка 5%')),
            ],
            options={
                'verbose_name': 'Скдка 5%',
                'verbose_name_plural': 'Скдка 5%',
            },
        ),
    ]