from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from journal.models import Journal


class JournalCreateView(CreateView):
    model = Journal
    fields = ('title', 'content',)
    success_url = reverse_lazy('journal:list')

    def form_valid(self, form):
        if form.is_valid:
            new_journal = form.save()
            new_journal.slug = slugify(new_journal.title)
            new_journal.save()

        return super().form_valid(form)


class JournalUpdateView(UpdateView):
    model = Journal
    fields = ('title', 'content',)
    # success_url = reverse_lazy('journal:list')

    def form_valid(self, form):
        if form.is_valid:
            new_journal = form.save()
            new_journal.slug = slugify(new_journal.title)
            new_journal.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('journal:view', args=[self.kwargs.get('pk')])


class JournalListView(ListView):
    model = Journal

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published_is=False)
        return queryset


class JournalDetailView(DetailView):
    model = Journal

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object


class JournalDeleteView(DeleteView):
    model = Journal
    success_url = reverse_lazy('journal:list')
