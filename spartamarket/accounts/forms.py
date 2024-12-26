# forms 는 models 과 관련됨
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'profile_image', 'password1', 'password2'] # 비번 확인용 2

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["profile_image",]