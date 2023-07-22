from django import forms


class SingInForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.PasswordInput()
