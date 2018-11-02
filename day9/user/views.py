from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
# Create your views here.
from user.filter import ArticleFilter
from user.forms import UserRegisterForm, UserloginForm
from user.models import Article
from user.serializers import ArticleSerializer
from rest_framework import mixins,viewsets



class ArticleView(viewsets.GenericViewSet, mixins.ListModelMixin,
                  mixins.DestroyModelMixin, mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()  # 查询数据
    serializer_class = ArticleSerializer#序列化
    filter_class = ArticleFilter#过滤


    def perform_destroy(self, instance):
        instance.is_delete = 1
        instance.save()

    # def get_queryset(self):
    #     queryset = self.queryset
    #     #获取过滤参数
    #     title = self.request.query_params.get('title')
    #     return queryset.filter(title=title)


def test(request):
    return render(request, 'test.html')

def articles(request):
    return render(request,'all_article.html')
# def register(request):
#     if request.method == "GET":
#         print('GET成功')
#         return render(request, 'register.html')
#
#     if request.method == "POST":
#         data = request.POST
#         form = UserRegisterForm(data)
#         if form.is_valid():
#             User.objects.create_user(username=form.cleaned_data.get('name'),
#                                     password=form.cleaned_data.get('pw'))
#             return HttpResponseRedirect(reverse('user:login'))
#         else:
#             errors = form.errors
#             return render(request, 'register.html', {'error': errors})
#
#
# def login(request):
#     if request.method == "GET":
#         print('GET成功')
#         return render(request, 'login.html')
#
#     if request.method == "POST":
#         data = request.POST
#         form = UserloginForm(data)
#         if form.is_valid():
#
#             user = auth.authenticate(username=form.cleaned_data.get('name'), password=form.cleaned_data.get('pw'))
#             if user:
#
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('user:index'))
#
#             else:
#                 return render(request,'login.html',{'msg':'密码错误'})
#
#         else:
#             return render(request, 'register.html', {'error': form.errors})
#
#
# def index(request):
#     if request.method == 'GET':
#         auth.logout(request)
#         res = render(request,'index.html')
#         return res
#
#
# class HttpRsponse(object):
#     pass
#
#
# def add_article(request):
#     if request.method == 'GET':
#         return render(request,'articles.html')
#     if request.method == 'POST':
#         img = request.FILES.get('file')
#         title = request.POST.get('title')
#         desc = request.POST.get('desc')
#         Article.objects.create(img=img,title=title,desc=desc)
#         return HttpResponse("成功")
#
#
# def show_article(request, id):
#     if request.method == 'GET':
#         article = Article.objects.get(pk=id)
#         return render(request,'show_article.html',{'article':article})
#     if request.method == 'POST':
#         # img = request.FILES.get('img')
#         # title = request.POST.get('title')
#         # desc = request.POST.get('desc')
#         # Article.objects.create(img=img,title=title,desc=desc))
#         pass
#
#
# def articles(request):
#     if request.method == 'GET':
#         page = request.GET.get('page',1)
#         article = Article.objects.all()
#         paginator = Paginator(article,3)
#         article = paginator.page(page)
#         return render(request, 'arts.html', {'article': article})
#
#
#
#
