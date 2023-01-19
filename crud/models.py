from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_contact = models.CharField(max_length=20)
    email_id = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    student_username = models.CharField(max_length=30, default="")
    student_password = models.CharField(max_length=20, default="")
    
class Admin(models.Model):
    Admin_name = models.CharField(max_length=30, default="")
    contact = models.CharField(max_length=20, default="")
    email_id = models.CharField(max_length=30, default="")
    password = models.CharField(max_length=20, default="")
    admin_username = models.CharField(max_length=30, default="")
    admin_password = models.CharField(max_length=20, default="")