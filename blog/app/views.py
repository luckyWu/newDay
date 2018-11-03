from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Max
from app.forms import Category_Check
from app.functions import login_required
from app.models import User, Culumn
from app.serializers import CulumnSerializer
from rest_framework import mixins,viewsets
# Create your views here.


class Cul(viewsets.GenericViewSet, mixins.ListModelMixin,
                  mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = Culumn.objects.filter() # 查询数据
    serializer_class = CulumnSerializer#序列化


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


def back_category(request):
    return render(request, 'back/category.html')


def back_article(request):
    return render(request, 'back/article.html')


def back_comment(request):
    return render(request, 'back/category.html')


def back_article(request):
    return render(request, 'back/article.html')


def back_notice(request):
    return render(request, 'back/notice.html')


def add_notice(request):
    return render(request, 'back/add_notice.html')


def back_category(request):
    if request.method == "GET":
        return render(request, 'back/category.html')
    if request.method == "POST":
        data = request.POST
        form = Category_Check(data)
        if form.is_valid():
            Culumn.objects.create(culumn_name=form.cleaned_data.get('name'),
                                  culumn_alias=form.cleaned_data.get('alias'),
                                  culumn_father=form.cleaned_data.get('fid'),
                                  culumn_key=form.cleaned_data.get('keywords'),
                                  culumn_description=form.cleaned_data.get('describe'),
                                  )
        return render(request, 'back/category.html')


def add_article(request):
    return render(request, 'back/add_article.html')


def update_article(request):
    return render(request, 'back/update_article.html')