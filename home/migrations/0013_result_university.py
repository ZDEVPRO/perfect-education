# Generated by Django 4.1.1 on 2022-09-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_result_alter_topcourse_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='university',
            field=models.CharField(default='nima', max_length=600),
            preserve_default=False,
        ),
    ]