from django.urls import path

from catalog.views import contact, home

urlpatterns = [
    path('', home),
    path('', contact),
]