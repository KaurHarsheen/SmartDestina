# forms.py

from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    cpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone', 'password', 'cpassword']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        cpassword = cleaned_data.get("cpassword")

        if password != cpassword:
            raise forms.ValidationError("Passwords do not match.")
