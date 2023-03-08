# Библиотека DjangoAuthEmailPin

[На английском](README.md)

Бесплатная, с открытым исходным кодом библиотека DjangoAuthEmailPin
предназначена для беспарольной авторизации пользователей в админке Django.
Для входа в админку пользователям на емейл высылаются одноразовые коды.

## Установка

```bash
pip install django-admin-auth-emailpin
```

## Использование

Для рассылки кодов авторизации используется штатный способ рассылки емайл в Django.
Поэтому в файле `settings.py` вашего проекта необходимо указать данные используемого почтового сервера.

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

## Разработка

```
$ git clone git@github.com:vb64/django.admin.auth.emailpin
$ cd django.admin.auth.emailpin
$ make setup PYTHON_BIN=/path/to/python3
$ make tests
```
