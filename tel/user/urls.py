from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^regiester/',views.register),
    url(r'^login/',views.login,name='login'),
    url(r'^index/',views.index,name='index'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^form_register/',views.form_register,name='register')
]