# Generated by Django 3.0.3 on 2020-07-27 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200719_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_registered',
            field=models.DateField(blank=True, null=True),
        ),
    ]
