from django.shortcuts import render,get_object_or_404
from .models import *
from django.shortcuts import HttpResponse

def student(request):
    stu = Student.objects.all()
    teacher=Teacher.objects.all()
    data = {}
    data['stu'] = stu
    data['teacher'] = teacher
    return render(request, "All_data.html", data)

def student_detail(request,id):
    detail=Student.objects.filter(id=id).last()
   
    data={}
    data['detail']=detail
   
    return render(request,"detail.html",data)

def teacher_detail(request,id):
    teacher = Teacher.objects.get(id=id)
    students = teacher.teacher_name.all()

    data = {
        'teacher_detail': teacher,
        'students': students,
    }

   
    return render(request,"teacher_detail.html",data)



def verify(request):
    error_message = None
    if request.method=="POST":
        get_token = request.POST.get('token')
        print(get_token)
       
        if not get_token:
            error_message = "Token is required. Please provide a valid token."
            return HttpResponse(error_message)
        else:
           
            try:
                var=Certificate.objects.get(token=get_token)
                print(var)
                return HttpResponse('certificate found VERIFY!')
            except Certificate.DoesNotExist:
                error_message = "Certificate not found. Please check the token."
                return HttpResponse(error_message)


    else:
        error_message = None
        return render(request, "verify.html",{'error_message':error_message})






