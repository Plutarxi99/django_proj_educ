from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'pictures',)
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'pictures',)
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ProductTemplateView(TemplateView):
    model = Product
    template_name = 'catalog/contact.html'

    def post(self, request, *args, **kwargs):
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, email, message)

        return render(request, 'catalog/contact.html')
