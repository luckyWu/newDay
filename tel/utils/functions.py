from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from user.models import User,UserToken

#
# def login_require(func):
#
#     def check_login(*args,**kwargs):
#         token = args.COOKIES.get('token')
#         if not token:
#             return HttpResponseRedirect(reverse('user:login'))
#         user_token = UserToken.objects.filter(token=token).first()
#         if not user_token:
#             return HttpResponseRedirect(reverse('user:login'))
#
#         return func(*args,**kwargs)
#     return check_login



def login_require(func):

    def check_login(request):
        try:
            #验证cookie中session值是否存在
            #验证服务器ssion表中是否对应值
            #如果存在则获取是否设置的User_id值
             request.session.get('user_id');
        except Exception as e:
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)
    return check_login

from django.utils.deprecation import MiddlewareMixin#有些版本需要导入


