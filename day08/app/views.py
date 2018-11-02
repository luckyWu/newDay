from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from app.forms import UserloginForm
from app.models import MyUser
from django.contrib.auth.models import Permission,Group


def add_user_permission(request):
    if request.method == "GET":
        # 1.创建用户
        suser = MyUser.objects.create_user(username='coco', password='123')
        permissions = Permission.objects.filter(codename__in=['add_my_user','all_my_user']).all()

        for permission in permissions:
            suser.user_permissions.add(permission)

        return HttpResponse('sucess!!!')


        # 2.指定创建的用户，分配权限


        # 3.删除用户权限




def index(request):
    if request.method == "GET":
        return render(request,'index.html')


def add_group_permission(request):
    if request.method == "GET":
        group = Group.objects.create(name='审核组')
        permissions = Permission.objects.filter(codename__in=['change_my_user_username', 'change_my_user_password''all_my_user']).all()
        for permission in permissions:
            group.permissions.add(permission)

        return HttpResponse('good!!!')


def add_user_group(request):
    if request.method == "GET":
        suser = MyUser.objects.get(username='coco')
        group = Group.objects.get(name='审核组')
        suser.groups.add(group)
        return HttpResponse('good!!!')


def show_user_permissions(request):
    if request.method == "GET":
        user = MyUser.objects.filter(username='coco').first()
        return render(request,'permissions.html',{'user':user})


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":

        form = UserloginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get('name'),
                                       password=form.cleaned_data.get('pw'))
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('app:my_index'))
            else:
                return render(request, 'login.html')

        else:
            return render(request, 'login.html', {'msg': form.errors})



def my_index(request):
    if request.method == "GET":
        return render(request, 'my_index.html')

#@permission_required()
# def new_index(request):
#     if request.method == "GET":
#         return HttpResponse('成功！！~~')