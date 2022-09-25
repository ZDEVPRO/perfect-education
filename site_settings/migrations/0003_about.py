# Generated by Django 4.1.1 on 2022-09-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_alter_homescreen_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=600)),
                ('title', models.CharField(max_length=600)),
                ('description', models.TextField()),
                ('button1_name', models.CharField(max_length=300)),
                ('button1_link', models.CharField(max_length=1000)),
                ('button2_name', models.CharField(max_length=300)),
                ('button2_link', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Biz haqimizda',
                'verbose_name_plural': 'Biz haqimizda',
            },
        ),
    ]
