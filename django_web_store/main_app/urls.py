from django.urls import path
from main_app.views import index


urlpatterns = [
    path('', index, name='show-index-page'),
]
