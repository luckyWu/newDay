from django import forms
from django.contrib.auth.models import User
from app.models import MyUser


class UserloginForm(forms.Form):
    name = forms.CharField(max_length=10, min_length=2, required=True, error_messages={'max_length': '长度要大于2', 'required': '注册姓名必填'})
    pw = forms.CharField(max_length=30, required=True)

    def clean(self):
        user = MyUser.objects.filter(username=self.cleaned_data.get('name')).first()
        if not user:
            raise forms.ValidationError({'name': '没有该账号'})
        return self.cleaned_data