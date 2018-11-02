"""day2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_grade/',views.add_grade),
    #127.0.0.1:8000/hello
    url(r'^hello/',views.hello),
    url(r'^create_stu/',views.create_stu),
    url(r'^sel_stu/',views.sel_stu),
    url(r'^del_stu/',views.del_stu),
    url(r'^update_stu',views.update_stu),
    url(r'^all_stu/',views.all_stu),
    url(r'^add_info/',views.add_info),
    url(r'^sel_info_by_stu/',views.sel_info_by_stu),
    url(r'^sel_stu_grade/', views.sel_stu_grade),
    url(r'^sel_stu_by_info/',views.sel_stu_by_info),
    url(r'^add_course/', views.add_course),
    url(r'^add_stu_course/',views.add_stu_course)

]
