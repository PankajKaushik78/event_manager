from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class UserCodeField(UserCreationForm):
#     Code = forms.CharField(max_length=120)

#     class Meta:
#         model = User
#         fields = ['Code']
