# Generated by Django 3.2.13 on 2022-05-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220518_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]