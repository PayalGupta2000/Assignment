from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.student,name="Students"),
    path('detail/<int:id>',views.student_detail,name="detail"),
    path('teacher_detail/<int:id>',views.teacher_detail,name="teacher_detail"),
    path('verify/',views.verify,name="verify")
   
]
