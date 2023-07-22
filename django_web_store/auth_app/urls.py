from django.urls import path
from auth_app.views import index
from auth_app.views import AuthSingInView

app_name = "auth"
urlpatterns = [
    path('', index, name='index-page'),
    path('login/', AuthSingInView.as_view(), name='login-page'),
]
