from django.urls import path
from auth_app.views import index


urlpatterns = [
    path('', index, name='index-page'),
]
