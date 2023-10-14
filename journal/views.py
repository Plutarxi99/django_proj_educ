from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from journal.models import Journal

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


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
        # queryset = queryset.filter(published_is=True)
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


def is_publish(request, pk):
    journal_item = get_object_or_404(Journal, pk=pk)
    if journal_item.published_is:
        journal_item.published_is = False
    else:
        journal_item.published_is = True
    journal_item.save()

    return redirect(reverse('journal:list'))


# def drop_mail(request, pk):
#     journal_view = get_object_or_404(Journal, pk=pk)
#     if journal_view.count_view > 10:
#         return send_mail('Nice dude',
#                          "Ты достиг 100 просмотров на публикации",
#                          "shievanov@bk.ru",
#                          ["shievanov.egor@yandex.ru"],
#                          fail_silently=False,
#                          )


def send_email(request, pk):
    # journal_view = get_object_or_404(Journal, pk=pk)
    subject = request.POST.get("subject", "Nice dude")
    message = request.POST.get("message", "Ты достиг 100 просмотров на публикации")
    from_email = request.POST.get("from_email", "shievanov.egor@yandex.ru")
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["egor.shievanov@gmail.com"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return redirect(reverse('journal:list'))
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse("Make sure all fields are entered and valid.")
