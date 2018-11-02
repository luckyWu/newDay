from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_required(func):
    def check(args):
        if not args.session.get('user_id'):
            return HttpResponseRedirect(reverse('blog:login'))
        return func(args)
    return check

