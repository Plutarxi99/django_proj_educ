from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Product, Category
from django.db import connection


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/view.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'pictures',)
    success_url = reverse_lazy('catalog:home')


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
