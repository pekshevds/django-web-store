from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView

from auth_app.forms import SingInForm


class AuthSingInView(TemplateView):
    template_name = "auth_app/login.html"

    def get(self, request, *args, **kwargs):

        context = {
            "form": SingInForm(),
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):

        form = SingInForm(request.POST)
        if form.is_valid():
            print("form is valid")
        return redirect("auth:login-page")


def index(request, *args, **kwargs):

    context = {
        'items': range(5000),
    }
    return render(request, template_name="auth_app/index.html", context=context)
