from django.urls import path
from journal.apps import JournalConfig
from journal.views import JournalCreateView, JournalListView, JournalDetailView, JournalUpdateView, JournalDeleteView

app_name = JournalConfig.name


urlpatterns = [
    path('create/', JournalCreateView.as_view(), name='create'),
    path('', JournalListView.as_view(), name='list'),
    path('view/<int:pk>/', JournalDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', JournalUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', JournalDeleteView.as_view(), name='delete'),
    # path('', home, name='home').
]