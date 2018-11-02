from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=10,null=True,unique=True)
    s_age = models.IntegerField(default=20)
    s_gender = models.BooleanField(default=1)
    grade = models.ForeignKey(Grade, null=True)
    class Meta:
        db_table = 'student'

class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True)
    class Meta:
        db_table = 'grade'

class Course(models.Model):
    c_name = models.CharField(max_length=10,unique=True)
    class Meta:
        db_table = 'course'

class StudentInfo(models.Model):
    phone = models.CharField(max_length=11,null=True)
    address = models.CharField(max_length=100)
    stu = models.OneToOneField(Student)

    class Meta:
        db_table = 'student_info'



