from django import template
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '#'

# @register.simple_tag
# def send_email(request, pk):
#     # journal_view = get_object_or_404(Journal, pk=pk)
#     subject = request.POST.get("subject", "Nice dude")
#     message = request.POST.get("message", "Ты достиг 100 просмотров на публикации")
#     from_email = request.POST.get("from_email", "shievanov.egor@yandex.ru")
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ["egor.shievanov@gmail.com"])
#         except BadHeaderError:
#             return HttpResponse("Invalid header found.")
#         return redirect(reverse('journal:list'))
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse("Make sure all fields are entered and valid.")


