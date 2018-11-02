from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^add_user_permission/', views.add_user_permission),
    url(r'^index', views.index, name='index'),
    url(r'^add_group_permission/', views.add_group_permission),
    url(r'^add_user_group/',views.add_user_group),
    url(r'^show_user_permissions/', views.show_user_permissions),
    url(r'^my_index/', views.my_index,name='my_index'),
    url(r'^login/', views.login,name='login')
]