from django import forms


class SingInForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.PasswordInput()


class SingUpForm(forms.Form):

    username = forms.CharField(max_length=150)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    email = forms.EmailInput()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
