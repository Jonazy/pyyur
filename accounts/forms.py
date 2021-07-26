from django import forms
from .models import CustomUser, Profile
from django.core.exceptions import ValidationError


class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=14, min_length=6, required=True)
    user_type = forms.CharField(max_length=14)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password is None or len(password) < 6:
            raise forms.ValidationError('Password must me greater than or equal 6 characters')
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match')

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=20, required=True)
    password = forms.CharField(max_length=14, min_length=6, required=True)


