# DjangoAuthEmailPin library

[In Russian](READMEru.md)

The free, open-source DjangoAuthEmailPin library is designed for password-free user authorization in the Django admin panel.
One-time codes are sent to users by email to enter the admin area.

## Installation

```bash
pip install django-admin-auth-emailpin
```

## Usage

To send authorization codes, the regular way of [sending email in Django](https://docs.djangoproject.com/en/dev/topics/email/) is used.
Therefore, in the `settings.py` file of your project, you must specify the details of the mail server used.

```python
# settings.py
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

## Development

```
$ git clone git@github.com:vb64/django.admin.auth.emailpin
$ cd django.admin.auth.emailpin
$ make setup PYTHON_BIN=/path/to/python3
$ make tests
```
