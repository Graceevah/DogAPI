# Generated by Django 4.2.6 on 2023-10-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogapi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='dog',
            name='color',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dog',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
