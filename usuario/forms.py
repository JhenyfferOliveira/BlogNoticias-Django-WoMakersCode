
from django import forms
from usuario.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'email', 'senha', 'role']


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)