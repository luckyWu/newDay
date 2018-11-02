
from user import views
from django.conf.urls import url

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('article', views.ArticleView)
urlpatterns = [
     # url('^register/', views.register, name='register'),
     # url('^login/', views.login, name='login'),
     # url(r'^index/', views.index, name='index'),
     url(r'^articles/', views.articles, name='articles'),
     url(r'^test/', views.test, name='test'),
     # url(r'show_article/(\d+)',views.show_article,name='show'),
     # url(r'articles/',views.articles,name='articles')

]
urlpatterns += router.urls