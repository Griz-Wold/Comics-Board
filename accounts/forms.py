from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PicturaUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = PicturaUser
        fields = [
            'username',
            'avatar',
            'email',
            'password1',
            'password2'
        ]