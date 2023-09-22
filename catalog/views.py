from django.shortcuts import render

from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # а также передается информация, которую заполнил пользователь
        print(name, email, message)
    return render(request, 'catalog/contact.html')
