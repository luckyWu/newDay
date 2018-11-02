
from user import views
from django.conf.urls import url

urlpatterns = [
     url('^register/', views.register, name='register'),
     url('^login/', views.login, name='login'),
     url(r'^index/', views.index, name='index'),
     url(r'^add_article/', views.add_article, name='add_article'),
     url(r'show_article/(\d+)',views.show_article,name='show'),
     url(r'articles/',views.articles,name='articles')

]