# Generated by Django 3.1 on 2020-10-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_auto_20200930_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='count_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solution',
            name='count_4',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
