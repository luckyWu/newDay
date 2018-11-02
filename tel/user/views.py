from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from user.models import User, UserToken
import random
from utils.functions import login_require


# from random import randint
# Create your views here.

def register(request):
    if request.method == "GET":
        print('GET成功')
        return render(request, 'register.html')

    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('pw')
        confirm = request.POST.get('pw1')
        # 2.检验是否完整
        if not all([name, password, confirm]):
            msg = '请填写完整参数！！！'
            return render(request, 'register.html', {'msg': msg})
        if User.objects.filter(name=name).first():
            msg = '改账号已注册！！'
            return render(request, 'register.html', {'msg': msg})
        print("成功！！！！！！！！！！！！！！！！")
        if confirm != password:
            msg = '密码不一致！！'
            return render(request, 'register.html', {'msg': msg})
        # 注册
        User.objects.create(name=name, password=password)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        pw = request.POST.get('pw')

        if not all([name, pw]):
            msg = '请填写完整'
            return render(request, 'login.html', {'msg': msg})
        user = User.objects.filter(name=name).first()
        if not user:
            msg = '没有该账号！！'
            return render(request, 'login.html', {'msg': msg})
        pw = User.objects.filter(password=pw).first()
        if not pw:
            msg = '密码错误！！'
            return render(request, 'login.html', {'msg': msg})
        #
        # res = HttpResponseRedirect(reverse('user:index'))
        # token = ''
        # s = '12222222222222222222222222213swkladncxx'
        # for i in range(25):
        #     token += random.choice(s)
        # res.set_cookie('token', token, max_age=6000)
        # # 存TOKEN
        # user_token = UserToken.objects.filter(user=user)
        # if not user_token:
        #     UserToken.objects.create(token=token, user=user)
        # else:
        #     pass
            # user_token.token =
        # 使用cookie + session
        # 向django_ssion表中存session值
        request.session['user_id'] = user.id
        return HttpResponseRedirect(reverse('user:index'))


# @login_require
def index(request):
    del request.session['user_id']
    return render(request, 'index.html')


# @login_require
def logout(request):
    if request.method == 'GET':
        res = HttpResponseRedirect(reverse('user:login'))
        # 删除浏览器cookie
        res.delete_cookie('token')
        token = request.COOKIES.get('token')
        UserToken.objects.filter(token=token).delete()
        return res


from user.forms import UserRegisterForm


# login_require(func)(request)
def form_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        data = request.POST
        form = UserRegisterForm(data)
        if form.is_valid():
            User.objects.create(name=form.cleaned_data.get('name'),
                                password=form.cleaned_data.get('pw'))
            return HttpResponseRedirect(reverse('user:login'))
        else:
            errors = form.errors
            return render(request, 'register.html', {'error': errors})
