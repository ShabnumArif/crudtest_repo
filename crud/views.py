from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import random
from crud.models import Admin,Student
# Create your views here.

def admin_login(request):
    return render(request,'crud1/admin_login.html')


def student_login(request):
     msg = ""
     if request.method == 'POST':
          student_username = request.POST['username']
          student_password = request.POST['password']
          try:
               user = Student.objects.get(email_id = student_username, password = student_password)
               request.session['student'] = user.id
               return redirect('crud:student_home')
          except:
               msg = "Username or Password incorrect"
     return render(request,'crud1/student_login.html',{'msg':msg})
   


def admin_login(request):
    msg = ""
    if request.method == 'POST':
          admin_name = request.POST['name']
          password = request.POST['password']
          try:
               user = Admin.objects.get(email_id = admin_name, password = password)
               request.session['admin'] = user.id
               return redirect('crud:admin_home')
          except:
               msg = "Username or Password incorrect"
    return render(request,'crud1/admin_login.html',{'msg':msg})
    


def admin_home(request):
    return render(request,'crud1/admin_home.html')


def student_reg(request):
    if request.method == 'POST':
          student_name = request.POST['name']
          student_contact = request.POST['contact']
          email_id = request.POST['email']
          password = request.POST['password']
          
          student_username = random.randint(1111,9999)
          student_password = 'stu-' + student_name.lower() + str(student_username)
          message = 'hi your username is' + str(student_username) + 'and the temporary password is ' + student_password
     
     
          new_student = Student(
          student_name = student_name,email_id = email_id,
          password = password,
          student_contact =  student_contact,
          student_username = email_id, student_password = password)
        
          
          new_student.save()
         

    return render(request,'crud1/student_reg.html')

    


def student_update(request):
    return render(request,'crud1/student_update.html')


def student_home(request):
    return render(request,'crud1/student_home.html')


def admin_reg(request):
     if request.method == 'POST':
          admin_name = request.POST['name']
          contact = request.POST['contact']
          email_id = request.POST['email']
          password = request.POST['password']
          
          admin_username = random.randint(1111,9999)
          admin_password = 'adm-' + admin_name.lower() + str(admin_username)
          message = 'hi your username is' + str(admin_username) + 'and the temporary password is ' + admin_password
     
          new_admin = Admin(
          Admin_name = admin_name,email_id = email_id,
          password = password,
          contact = contact,
          admin_username = email_id, admin_password = password)
        
          
          new_admin.save()
    
     return render(request,'crud1/admin_reg.html')


def active_student(request):
    return render(request,'crud1/active_student.html')


def register(request):
    return render(request,'crud1/register.html')

