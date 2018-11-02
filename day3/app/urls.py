from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^index/',views.index,name='aindex'),
    url(r'^all_stu/',views.all_stu,name='allstu'),
    url(r'^index_redirect/',views.index_redirect),
    url(r'^edit_stu/(\d+)',views.edit_stu,name='edit')

]