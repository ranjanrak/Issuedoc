from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Main, Content,Issue

class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = ['title','detail','image',]


class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'detail'] 

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['date','detail','rectify','tag','tag2']                

class UserForm(forms.ModelForm):
	password =forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields =['username','email','password']        