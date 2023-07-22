from django.urls import path
from catalog_app.views import index


urlpatterns = [
    path('', index, name='index-page'),
]
