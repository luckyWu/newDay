from django.db.models import Q,F
from django.shortcuts import render
# Create your views here.
from app.models import Student,StudentInfo,Grade,Course
from django.http import HttpResponse



def hello(request):
    return HttpResponse('html')

#
# def create_stu(request):
#     stu = Student()
#     stu.s_name="小李1"
#     stu.s_age = 20
#     stu.save()
#     return HttpResponse("添加成功！！！！！！！")


def create_stu(request):
    # Student.objects.create(s_name="小红1")
    # Student.objects.create(s_name="小红2")
    # Student.objects.create(s_name="小红3")
    # Student.objects.create(s_name="小红4")
    # Student.objects.create(s_name="小红5")
    # Student.objects.create(s_name="小红6")
    Student.objects.create(s_name="荆轲",class1="python")

    return HttpResponse("成功！！！！！！")

def sel_stu(request):
    # stu = Student.objects.all()
    #
    # stu1 = Student.objects.filter(id=1)#和pk=1同效；

    #stu.values('s_name','s_age')#所有对象的字段

    # stu1 = Student.objects.filter(s_name="小红").first()#不存在不会报错；

    # stu = Student.objects.get(s_age=20)#不存在会报错，此方法只能返回一个;

    # stu = Student.objects.filter(s_age=20).filter(s_name="小明")#

    stu = Student.objects.filter(yuwen__gt=F('shuxue')+10)#语文比数学大十分
    print(stu)
    stu = Student.objects.filter(s_age=20,s_name="姓名")  #

    stu = Student.objects.filter(Q(s_age = 18) | Q(s_name = "小明"))  #或查询：& ~

    # stu = Student.objects.filter(s_name__contains='1')#模糊查询；
    #
    # stu = Student.objects.filter(s_name__startswith="小")#以小开头；
    #
    # stu = Student.objects.filter(s_name__endswith="1")#以1结尾；
    #
    # stu = Student.objects.filter(s_age__gt=18)#大于
    #
    # stu = Student.objects.filter(s_age__lt=18)#小于
    #
    # stu = Student.objects.order_by('-id') #降序'id'升序
    #
    # stu = Student.objects.exclude(s_age=18)#查询不满足条件的
    #
    # print(len(stu))#stu.count()统计个数
    # print(stu.count(),"count")
    # stu = [stu.s_name for stu in stu]
    # print(stu)
    # for i in stu:
    #     print(i.s_name, end="\t")
    #     print(i.s_age, end="\t")
    #     print(i.s_gender)
    return HttpResponse("123")


def del_stu(request):
    Student.objects.filter(s_name="小红").delete()
    return HttpResponse("删除成功！！！！！！！！！！！")


def update_stu(request):
    # stu = Student.objects.filter(s_name="小红1").first()
    # stu.s_name = "大红1"
    stu = Student.objects.filter(s_name="大红1").update(s_name="金科")

    stu.save()
    return HttpResponse("修改成功！！！！！")

def all_stu(request):
    stu = Student.objects.all()
    return render(request,'stu1.html',{'student':stu})


def add_info(request):
    if request.method == 'GET':#method获取HTTP方式
        return render(request, 'info.html')
    elif request.method == 'POST':
        #获取页面中提交的手机号码和地址
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        stu_id = request.GET.get('stu_id')
        #保存
        StudentInfo.objects.create(phone=phone,address=address,stu_id=stu_id)
        return HttpResponse('创建信息成功！stu_id=%s' %( stu_id))

def sel_info_by_stu(request):
    if request.method == "GET":
        stu = Student.objects.get(s_name="小明")
        #第一种
        #info = StudentInfo.objects.filter(stu_id = stu.id)
        #info = StudentInfo.objects.filter(stu=stu)
        #第二种：info = stu.studentinfo
        pass




def sel_stu_by_info(request):
    if request.method == "GET":
        info = StudentInfo.objects.get(phone='15723066578')
        student = info.stu

def add_grade(request):
    if request.method == "GET":
        name = ['数学','英语','物理']
        for name1 in name:
            Grade.objects.create(g_name=name1)
        return HttpResponse('456')

def sel_stu_grade(request):
    if request.method == "GET":
        #1.通过学生查找班级
        stu = Student.objects.filter(s_name='小明').first()
        stu.grade
        #2.通过班级查找学生
        grade = Grade.objects.get(g_name='英语')
        grade.student_set.all()
        return HttpResponse("sel_stu_grade")

def add_course(request):
    sname = ['大学英语','美术鉴赏','日语']
    for name in sname:
        Course.objects.create(c_name=name)


def add_stu_course(request):
    if request.method == "GET":
        cous = Course.objects.all()
        return render(request,'course.html',{'cous':cous})
    if request.method == "POST":
        c_id = request.POST.get('www')
        s_id = request.GET.get('stu_id')

        stu = Student.objects.get(pk=s_id)
        cour =Course.objects.get(pk=c_id)
        stu.course_set.add(cour)
        return HttpResponse("chenggong!!!!")


def show_stu_course(request):
    if request.method == "GET":
        cous = Course.objects.all()
        return render(request,'course.html',{'cous':cous})
    if request.method == "POST":
        c_id = request.POST.get('www')
        s_id = request.GET.get('stu_id')

        stu = Student.objects.get(pk=s_id)
        cour =Course.objects.get(pk=c_id)
        stu.course_set.add(cour)
        return HttpResponse("chenggong!!!!")


