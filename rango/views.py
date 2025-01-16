from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
# Create your views here.

def index(request):
    category_list = Category.objects.order_by('-name')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunch, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list

    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)
