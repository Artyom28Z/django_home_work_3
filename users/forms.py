from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm
from django import forms
from catalog_2.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class ResetPasswordForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ['email', ]


class UserProfileForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'phone', 'avatar', 'country', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
