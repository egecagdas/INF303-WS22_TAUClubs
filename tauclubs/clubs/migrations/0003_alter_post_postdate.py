# Generated by Django 3.2.10 on 2022-12-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20221203_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]