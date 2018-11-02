from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.
from django.shortcuts import render
from app.models import Student


def index(request):
    a=1
    if request.method == 'GET':
        res = HttpResponseRedirect('/all_stu/')
        return res
        return render(request, 'index.html')



def all_stu(request):
    if request.method == 'GET':
       stu  =  Student.objects.all()
       content_h2  = '<h2>天气正好</h2>'
       return render(request,'stu.html',{'stus':stu,'cont':content_h2})


def index_redirect(request):
    if request.method == 'GET':
        #实现重定向1.地址是硬编码
       # return HttpResponseRedirect('/app/index/')
        #第二种重定向：使用反向解析reverse('namespace:name')

        return HttpResponseRedirect(reverse('dy:aindex'))# alt+enter

def edit_stu(request,id):
    if request.method == 'GET':
        stu = Student.objects.get(pk=id)
        return render(request,'edit.html',{'stu':stu})
    if request.method == 'POST':
        stu = Student.objects.get(pk=id)

        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        print(type(name))
        stu.s_age = age
        stu.s_name = name
        stu.save()
        return HttpResponse("成功!!!!!!!!!!!!!~~~~~~~~~~~~~~~~")



