from django.shortcuts import render
from catalog_app.models import Category


def index(request):

    context = {
        'items': range(5000),
        'categories': Category.fetch_top_level_categories()
    }
    return render(request, template_name="index_app/index.html", context=context)
