from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.functions import login_required
from app.models import User
# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'front/index.html')


def share(request):
    return render(request, 'front/share.html')


def about(request):
    return render(request, 'front/about.html')


def gbook(request):
    return render(request, 'front/gbook.html')


def info(request):
    return render(request, 'front/info.html')


def infopic(request):
    return render(request, 'front/infopic.html')


def list(request):
    return render(request, 'front/list.html')


def login(request):
    if request.method == "GET":
        return render(request, 'back/login.html')
    if request.method == "POST":
        a = 1
        name = request.POST.get('username')
        pw = request.POST.get('userpwd')
        user = User.objects.filter(name=name).first()
        password = User.objects.filter(pw=pw).first()

        if user and password:
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('blog:backindex'))
        else:
            return render(request, 'back/login.html')


def backindex(request):
        if not request.session.get('user_id'):
            return HttpResponseRedirect(reverse('blog:login'))
        return render(request,'back/index.html')

