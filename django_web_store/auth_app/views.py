from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from auth_app.models import User
from django.contrib.auth import get_user_model


class AuthSingInView(LoginView):
    template_name = "auth_app/signin.html"
    authentication_form = AuthenticationForm

    def get(self, request, *args, **kwargs):

        context = {"form": self.authentication_form()}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = self.authentication_form(request=request, data=request.POST)
        if not form.is_valid():
            context = {
                "form": form,
                "errors": form.errors,
            }
            return render(request, template_name=self.template_name, context=context)
        return redirect("index:index-page")


class AuthSingUpCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class AuthSingUpView(LoginView):
    template_name = "auth_app/signup.html"
    authentication_form = AuthSingUpCreationForm

    def get(self, request, *args, **kwargs):

        context = {
            "form": self.authentication_form(),
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = self.authentication_form(data=request.POST)
        if not form.is_valid():
            context = {
                "form": form,
                "errors": form.errors,
            }
            return render(request, template_name=self.template_name, context=context)
        form.save()
        return redirect("auth:sign-in-page")


class AuthSingOutView(LogoutView):
    pass


def index(request, *args, **kwargs):

    context = {
        'items': range(5000),
    }
    return render(request, template_name="auth_app/index.html", context=context)
