from django.urls import path
from index_app.views import index

app_name = "index"
urlpatterns = [
    path('', index, name='index-page'),
]
