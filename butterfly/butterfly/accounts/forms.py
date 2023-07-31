from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from butterfly.accounts.models import ButterflyUser

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = ButterflyUser
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class LogInForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder': 'Username',
            }))

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Password'
            }
        )
    )


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'profile_picture', 'email']
