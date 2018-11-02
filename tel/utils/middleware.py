

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import UserToken


class Test1Middleware(MiddlewareMixin):
    def process_request(self,request):
        not_check = ['/user/login/','/user/register/']
        path = request.path
        if path in not_check:
            return None
        token = request.COOKIES.get('token')
        if not token:
            return HttpResponseRedirect(reverse('user:login'))
        user_token = UserToken.objects.filter(token=token).first()
        if not user_token:
            return HttpResponseRedirect(reverse('user:login'))
        #给全局request添加user
        request.user = user_token.user

        return None