# Generated by Django 4.1.5 on 2023-01-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='student_username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
