from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView

from auth_app.forms import SingInForm
from auth_app.forms import SingUpForm


class AuthSingInView(TemplateView):
    template_name = "auth_app/signin.html"

    def get(self, request, *args, **kwargs):

        context = {
            "form": SingInForm(),
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = SingInForm(request.POST)
        if not form.is_valid():
            return redirect("auth:sign-in-page")
        return redirect("index:index-page")


class AuthSingUpView(TemplateView):
    template_name = "auth_app/signup.html"

    def get(self, request, *args, **kwargs):

        context = {
            "form": SingUpForm(),
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = SingUpForm(request.POST)
        if not form.is_valid():
            return redirect("auth:sign-up-page")
        return redirect("index:index-page")


class AuthSingOutView(TemplateView):

    def get(self, request, *args, **kwargs):
        return redirect("auth:sign-in-page")


def index(request, *args, **kwargs):

    context = {
        'items': range(5000),
    }
    return render(request, template_name="auth_app/index.html", context=context)
