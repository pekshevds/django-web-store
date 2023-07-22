from django.urls import path
from order_app.views import index


urlpatterns = [
    path('', index, name='index-page'),
]
