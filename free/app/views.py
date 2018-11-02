from django.db.models import Q
from django.shortcuts import render,HttpResponse
from app.models import Student,Grade,Course
# Create your views here.
def dele(request):
	Student.objects.filter(s_name='小明').delete() #删除小明那一行数据，filter用来筛选数据
	return HttpResponse('删除成功')

def update(request):
    #方式1：
	#Student.objects.filter(s_name='小明').update(s_name='大明')
    #方式2：
    stu = Student.objects.get(s_name='小红')
    stu.s_name = '大红'
    stu.save()
    return HttpResponse('删除成功')


def sel(request):
    Student.objects.all()#获取所有对象;
    stu = Student.objects.filter(id=1) # 获取ID为1的对象和pk=1同效；不存在报错
    stu = Student.objects.get(s_age=20)  # 不存在会报错，此方法只能返回一个对象;
    stu = Student.objects.filter(s_age=20, s_name="小明")#筛选多个条件；

    stu = Student.objects.filter(s_name__contains='1')#模糊查询；
    stu = Student.objects.filter(s_name__startswith="小")#以小开头；
    stu = Student.objects.filter(s_name__endswith="1")#以1结尾；

    stu = Student.objects.filter(s_age__gt=18)#大于
    stu = Student.objects.filter(s_age__lt=18)#小于

    stu = Student.objects.filter(Q(s_age=18) | Q(s_name="小明"))  # 或查询：&(与） ~ （非）需要导入 Q模块
    return HttpResponse('成功')


def index(request):
    return render(request,'index.html')

