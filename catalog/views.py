from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db import IntegrityError
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import ProductForm, VersionForm, VersionFormProduct
from .models import Product, Version, Category
from django.contrib import messages
from django.http import JsonResponse, HttpResponse, Http404

from .services import cache_category


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            context_data['category_list'] = cache_category()
        return context_data

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = Category.objects.all()
    #     if settings.CACHE_ENABLED:
    #         key = 'categories'
    #         cache_data = cache.get(key)
    #         if cache_data is None:
    #             cache_data = queryset
    #             cache.set(key, cache_data)
    #             print(cache_data)
    #         return cache_data
    #
    #     return queryset


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class VersionDetailView(LoginRequiredMixin, DetailView):
    model = Version


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    # fields = ('name', 'description', 'category', 'price', 'pictures',)
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.product_creator = self.request.user
        self.object.save()

        return super().form_valid(form)


# class VersionCreateView(CreateView):
#     model = Version
#     form_class = VersionForm
#     success_url = reverse_lazy('catalog:home')


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'price', 'pictures',)
    success_url = reverse_lazy('catalog:home')
    error_message = "Оставьте одну активную версию"
    permission_required = 'catalog.change_product'

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

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.request.user.is_superuser:
    #         return self.object
    #     elif self.object.product_creator != self.request.user:
    #         raise Http404
    #     else:
    #         return self.object

    # def has_permission(self):
    #     """
    #     Если у пользователя нет прав на редактирование выдаёт ошибку 403
    #     """
    #     perms = self.get_permission_required()
    #     product: Product = self.get_object()
    #     return self.request.user == product.product_creator

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_form(self):
        """
        Метод для скрытия полей редактирования продукта в edit, если пользователь не его создатель
        """
        form = super().get_form()
        if self.request.user != form.instance.product_creator:  # сравниваем авторизированного пользователя с создателем продукта
            enabled_fields = set()  # метод для добавления полей для чего ???
            if self.request.user.has_perm(
                    'catalog.change_name'):  # если у пользователя есть права на редактирования то разрешаем редактирование этого пользователя
                enabled_fields.add('name')  # добавляем поле для редактирования
            if self.request.user.has_perm('catalog.change_description'):
                enabled_fields.add('description')
            if self.request.user.groups.filter(name='Модератор').exists(): # Если пользователь принадлежит к группе "Модератор", то ему можно изменять поля
                enabled_fields.add('is_published')  # добавляем поле для редактирования

            if self.request.user.is_superuser:
                enabled_fields.add('price')  # добавляем поле для редактирования
                enabled_fields.add('category')  # добавляем поле для редактирования
                enabled_fields.add('is_published')  # добавляем поле для редактирования

            for field_name in enabled_fields.symmetric_difference(form.fields):
                form.fields[field_name].disabled = True
                form.errors.pop(field_name, None)

        return form


class VersionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.change_version'


# def index(request):
#     context = {'form': VersionForm()}
#     return render(request, 'version_form.html', context)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'


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
