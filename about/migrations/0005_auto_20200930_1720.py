# Generated by Django 3.1 on 2020-09-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20200930_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(null=True, upload_to='About/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(null=True, upload_to='Team/%Y/%m/%d/'),
        ),
    ]