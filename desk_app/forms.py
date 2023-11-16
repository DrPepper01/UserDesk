from django import forms
from django.contrib.auth.models import User

from .models import Comments


class CommentsForm(forms.ModelForm):

    title = forms.CharField(label='Ваш комментарий')

    class Meta:
        model = Comments
        fields = ['title']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


