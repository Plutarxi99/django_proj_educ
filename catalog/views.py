from django.db import IntegrityError
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import ProductForm, VersionForm, VersionFormProduct
from .models import Product, Version
from django.contrib import messages
from django.http import JsonResponse, HttpResponse


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class VersionDetailView(DetailView):
    model = Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'price', 'pictures',)
    success_url = reverse_lazy('catalog:home')


# class VersionCreateView(CreateView):
#     model = Version
#     form_class = VersionForm
#     success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'price', 'pictures',)
    success_url = reverse_lazy('catalog:home')
    error_message = "Оставьте одну активную версию"

    # def form_invalid(self, form):
    #     messages.error(self.request, self.error_message)
    #     return super().form_invalid(form)

    # def form_invalid(self, form):
    #     response = super().form_invalid(form)
    #     if self.request.accepts('catalog:home'):
    #         return response
    #     else:
    #         return JsonResponse(form.errors, status=400)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionFormProduct, extra=1)
        obj = self.object
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=obj)
        else:
            context_data['formset'] = VersionFormset(instance=obj)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')


# def index(request):
#     context = {'form': VersionForm()}
#     return render(request, 'version_form.html', context)


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
