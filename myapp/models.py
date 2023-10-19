from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=50)
   

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name=models.CharField(max_length=50)
    teacher_name=models.ManyToManyField('Teacher',blank=True,related_name="teacher_name")

    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    token=models.CharField(max_length=100,unique=True)
    file=models.FileField(upload_to="files")



