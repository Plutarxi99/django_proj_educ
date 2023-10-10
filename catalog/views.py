from django.shortcuts import render
from .models import Product, Category
from django.db import connection


def home(request):

    list_product = Product.objects.all()
    context = {
        "object_list": list_product
    }
    return render(request, 'catalog/home.html', context)


def contact(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, email, message)
    # context = {
    #     "title": 'Contact'
    # }
    return render(request, 'catalog/contact.html')


