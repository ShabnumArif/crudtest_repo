# Generated by Django 4.1.5 on 2023-01-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_student_student_password_student_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='admin_password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='admin',
            name='admin_username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
