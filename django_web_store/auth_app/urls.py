from django.urls import path
from auth_app.views import index
from auth_app.views import AuthSingInView
from auth_app.views import AuthSingUpView
from auth_app.views import AuthSingOutView

app_name = "auth"
urlpatterns = [
    path('', index, name='index-page'),
    path('signin/', AuthSingInView.as_view(), name='sign-in-page'),
    path('signup/', AuthSingUpView.as_view(), name='sign-up-page'),
    path('signout/', AuthSingOutView.as_view(), name='sign-out-page'),
]
