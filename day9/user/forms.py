from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    name = forms.CharField(max_length=10, min_length=2, required=True, error_messages={'min_length': '长度要大于2', 'required': '注册姓名必填'})#
    pw = forms.CharField(max_length=30, required=True, error_messages={'max_length': '长度要小于30', 'required': '密码必填'})
    pw1 = forms.CharField(max_length=30, required=True, error_messages={'max_length': '长度要小于30', 'required': '请确认密码'})

    def clean(self):

        name = self.cleaned_data.get('name')
        user = User.objects.filter(username=name).first()
        if user:
            raise forms.ValidationError({'name': '账号已注册'})
        if self.cleaned_data.get('pw') != self.cleaned_data.get('pw1'):
            raise forms.ValidationError({'pw': '密码不一致'})
        return self.cleaned_data


class UserloginForm(forms.Form):
    name = forms.CharField(max_length=10, min_length=2, required=True, error_messages={'max_length': '长度要大于2', 'required': '注册姓名必填'})
    pw = forms.CharField(max_length=30, required=True)

    def clean(self):
        user = User.objects.filter(username=self.cleaned_data.get('name')).first()
        if not user:
            raise forms.ValidationError({'name': '没有该账号'})
        return self.cleaned_data
