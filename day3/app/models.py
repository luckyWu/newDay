from django.db import models

# Create your models here.




class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'grade'


# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=20,unique=True)#定义s_name字段，varchar 类型，最长不超过6个字符，唯一；
    s_age= models.IntegerField(default=18)
    s_gender = models.BooleanField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    option_time = models.DateTimeField(auto_now=True)
    yuwen = models.DecimalField(decimal_places=1,max_digits=4,null=True)
    shuxue = models.DecimalField(decimal_places=1,max_digits=4,null=True)
    grade = models.ForeignKey(Grade,null=True)
    class Meta:
        db_table = 'student'#定义模型迁移到数据库中的表名；


class StudentInfo(models.Model):
    phone = models.CharField(max_length=11,null=True)
    address = models.CharField(max_length=100)
    stu = models.OneToOneField(Student)

    class Meta:
        db_table = 'student_info'


class Course(models.Model):
    c_name = models.CharField(max_length=10)
    stu = models.ManyToManyField(Student)

    class Meta:
        db_table = 'course'

