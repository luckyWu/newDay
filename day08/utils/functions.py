from django.http import HttpResponse

from app.models import MyUser


def check_permissions(func):
    def check(request):
        user  = MyUser.objects.filter(username='coco').first()
        u_p = user.user_permission.filter(codename='all_my_user').first()
        if u_p:
            return func(request)
        else:
            return HttpResponse('用户没有权限！')
    return check