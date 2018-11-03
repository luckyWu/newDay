
from django import forms
#
#
# class LoginCheck(forms.Form):
#     username = forms.CharField(max_length=10,required=True)
#     userpwd = forms.CharField( required=True)
#
#     def clean(self):
#         pass
from app.models import Culumn


class Category_Check(forms.Form):
    name = forms.CharField(error_messages={'name': 'name错误'})
    alias = forms.CharField(error_messages={'alias': 'lias错误'})
    fid = forms.CharField(error_messages={'fid': 'fid错误'})
    keywords = forms.CharField(error_messages={'key': 'key错误'})
    describe = forms.CharField(error_messages={'des': 'des错误'})

    def clean(self):
        cul = Culumn.objects.filter(culumn_name=self.cleaned_data.get('name')).first()
        if cul:
            raise forms.ValidationError({'name': '该栏目名已存在！'})
        else:
            return self.cleaned_data
