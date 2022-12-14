# Generated by Django 4.1.1 on 2022-09-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0007_about_image_homescreen_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=600)),
                ('email', models.CharField(max_length=600)),
                ('phone', models.CharField(max_length=600)),
            ],
            options={
                'verbose_name': 'Aloqa Malumotlari',
                'verbose_name_plural': 'Aloqa Malumotlari',
            },
        ),
    ]
