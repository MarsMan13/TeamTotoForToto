from django import forms
from .models import Community_post
from django.contrib.auth.models import User

class Signup_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class Login_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class Community_PostForm(forms.ModelForm):
    class Meta:
        model = Community_post
        fields = ('title', 'text',)