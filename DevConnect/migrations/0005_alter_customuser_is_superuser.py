# Generated by Django 5.0 on 2024-01-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DevConnect', '0004_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]