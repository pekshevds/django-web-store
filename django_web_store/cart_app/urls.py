from django.urls import path
from cart_app.views import index


urlpatterns = [
    path('', index, name='index-page'),
]
