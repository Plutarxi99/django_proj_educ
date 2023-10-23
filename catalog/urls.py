from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductTemplateView, VersionDetailView, VersionUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('contact/', ProductTemplateView.as_view(), name='contact'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    # path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('edit_version/<int:pk>/', VersionUpdateView.as_view(), name='edit_version'),
    path('view_version/<int:pk>/', VersionDetailView.as_view(), name='view_version'),
]