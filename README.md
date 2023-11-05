# django_proj_educ
Этот проект создан исключительно в образовательных целях и показано, то чему я научился в целях курса.
Проект написан с помощью фреймворка Django: https://github.com/django/django

Данный проект содержит в себе 3 приложения:
* **catalog**
* **journal**
* **users**

Добавлен файл https://github.com/Plutarxi99/django_proj_educ/blob/main/.env.sample (для использования надо привести к ввиду **<.env>**) с помощью, которого можно настроить работу проекта. В нем лежат настройки (далее идут примеры заполнения полей):
* **CACHE_ENABLED**=1 (Если записывать в кэш, иначе ставится 0)
* **CACHE_LOCATION**=redis://127.0.0.1:6379 (база данных для записи кэша)

* **DATABASE_LOGIN**='{
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "django_proj_educ",
    "USER": "postgres",
}' (словарь для подключения к базе данных. P.S. не забудь создать ее)

* **EMAIL_HOST_USER**=your.email@yandex.ru (Email с какого отправлять письмо)
* **EMAIL_HOST_PASSWORD**=rgergergersgsdrg (пароль приложения, получить можно тут https://id.yandex.ru/security/app-passwords)


* **EMAIL_BACKEND**=django.core.mail.backends.smtp.EmailBackend (объязательные настройки для отправки письма)
* **EMAIL_HOST**=smtp.yandex.ru
* **EMAIL_PORT**=465
* **EMAIL_USE_SSL**=True


* **SECRET_KEY**=django-insecure-hu213gr51uh234gbrtf34oqufg35835g3q5g (код генерируется автоматически при создании приложения)
* **EXCLUDE_WORD**="['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']" (список запрещенных слов)