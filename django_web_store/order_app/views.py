from django.shortcuts import render


def index(request):

    context = {
        'items': range(5000),
    }
    return render(request, template_name="order_app/index.html", context=context)
