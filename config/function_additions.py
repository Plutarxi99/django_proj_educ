def password():
    with open('YANDEX_MAIL_PASSWORD') as cont:
        value = cont.read()
    return value
