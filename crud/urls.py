from django.urls import path
from . import views

app_name = 'crud'
urlpatterns=[
   path('admin_login',views.admin_login,name="admin_login"),
   path('student_login',views.student_login,name="student_login"),
   path('admin_login',views.admin_login,name="admin_login"),
   path('admin_home',views.admin_home, name = "admin_home"),
   path('student_reg',views.student_reg, name = "student_reg"),
   path('student_update',views.student_update, name = "student_update"),
   path('',views.student_home, name = "student_home"),
   path('admin_reg',views.admin_reg, name = "admin_reg"),
   path('active_student',views.active_student, name = "active_student"),
   path('register',views.register, name = "register"),


]