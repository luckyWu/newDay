from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
# Create your views here.

from user.forms import UserRegisterForm, UserloginForm


def register(request):
    if request.method == "GET":
        #

        print('GET成功')
        return render(request, 'register.html')

    if request.method == "POST":
        data = request.POST
        form = UserRegisterForm(data)
        if form.is_valid():

            User.objects.create_user(username=form.cleaned_data.get('name'),
                                       password=form.cleaned_data.get('pw'))
            user = User.objects.get(username='巫岷骏')
            return render(request, 'index.html', {'user': user})
            # return HttpResponseRedirect(reverse('user:login'))
        else:
            errors = form.errors
            return render(request, 'register.html', {'error': errors})


def login(request):
    if request.method == "GET":
        print('GET成功')
        return render(request, 'login.html')

    a = 1

    if request.method == "POST":
        data = request.POST
        form = UserloginForm(data)
        if form.is_valid():

            user = auth.authenticate(username=form.cleaned_data.get('name'), password=form.cleaned_data.get('pw'))
            if user:

                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:index'))

            else:
                return render(request,'login.html',{'msg': '密码错误'})

        else:
            return render(request, 'register.html', {'error': form.errors})


def index(request):
    if request.method == 'GET':
        auth.logout(request)
        res = render(request,'index.html')
        return res
