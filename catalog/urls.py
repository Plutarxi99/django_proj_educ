from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductTemplateView, VersionDetailView, VersionUpdateView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('view/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='view'),
    path('contact/', cache_page(60)(ProductTemplateView.as_view()), name='contact'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    # path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('edit_version/<int:pk>/', VersionUpdateView.as_view(), name='edit_version'),
    path('view_version/<int:pk>/', cache_page(60)(VersionDetailView.as_view()), name='view_version'),
    path('list_category/', CategoryListView.as_view(), name='list_category'),
]