from .models import Message
from django import forms
from django.contrib.auth import get_user_model
from django.forms import PasswordInput, ModelForm


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']


# форма регистрации
class RegisterForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'nick']

    username = forms.CharField(min_length=3, max_length=10, required=True)
    nick = forms.CharField(min_length=1, max_length=20, required=True)
    password = forms.CharField(widget=PasswordInput(), required=True)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        # валидация паролей
        password = cleaned_data.get("password")

        # валидация никнейма
        username = self.cleaned_data.get("username")

        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError({'username': "Такой логин уже занят"})

        return cleaned_data
