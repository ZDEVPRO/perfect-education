# Generated by Django 4.1.1 on 2022-09-24 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
