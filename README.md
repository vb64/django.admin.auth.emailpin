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

The Django admin user model must have special fields to use the library.

-   `name`: primary email address for user.
-   `custom_email`: optional additional user email.
-   `is_active`: if this field is set to False, then the user is disabled in admin panel.

The library provides an abstract `User` class that defines these fields.
This class can be used as a base class when defining the user model of your project.

```python
# models.py
from django_admin_auth_emailpin.models import User

class MyUser(User):
    # Titles for fields in Django admin
    title_fld_name = "Login"
    title_fld_email = "Custom email"
    title_fld_active = "Active"
```

For user authorization using the library, your project must contain a model,
inherited from the `PinCode` class from the library.

```python
# models.py
from django_admin_auth_emailpin.models import PinCode

class Pin(PinCode):

```

The following methods need to be defined in this model.

### Method mail_secrets

Returns a tuple of three elements specifying the parameters for accessing the mail server.

-   address where authorization codes for the `admin` user (database superuser) will be sent
-   username to connect to the mail server
-   password to connect to the mail server

```python
# models.py

    @classmethod
    def mail_secrets(cls):
        return (
          'admin@example.com',
          'example.admin@gmail.com',
          'smtp-password',
        )
```

### Method mail_inacive

Gets an instance of the user model that is denied access to the admin panel (the `is_active` field is set to False).

Returns a tuple of three elements specifying the parameters of the email that will be sent to this user.

-   the address from which the email will be sent
-   email subject text
-   email body text

```python
# models.py

    @classmethod
    def mail_inacive(cls, user):
        return (
          "noreply@example.com",
          "Failed login at example.com.",
          "Your account {} is disabled. Ask for admin to solve issue.".format(user),
        )
```

### Method mail_login

Gets the model instance of the user who requested authorization and the model instance of the authorization code generated for that user.

Returns a tuple of three elements defining the parameters of the email with authorization data that will be sent to this user.

-   the address from which the email will be sent
-   email subject text
-   email body text

```python
# models.py

    @classmethod
    def mail_login(cls, user, pin):
        return (
          "noreply@example.com",
          "Login at example.com",
          "To login as {} use PIN code: {}".format(user, pin.code),
        )
```

### User Authorizations

To start authorization of a user named `username`, you need to call the `Pin.auth` method,
passing it the model class and username.

If there is a user with this name in the database and he is allowed to enter the admin panel (field `is_active=True`),
a one-time authorization code will be generated for this user and an email with this code will be sent to the user.

The `Pin.auth` method will return `True` in this case.

If the user with the given name is not in the database or he is denied access to the admin panel (field `is_active=False`),
the `Pin.auth` method will return `False`.

```python
# views.py
from .models import MyUser, Pin

    assert Pin.auth(MyUser, 'username')
```

To complete the authorization, you need to get the value of the authorization code from the user and call the `Pin.is_valid` method.
This method should be passed the name of the authorized user and the authorization code.

If a valid code value is used, the method will return `True` and the authorization code used in the call will become invalid.

## Development

```
$ git clone git@github.com:vb64/django.admin.auth.emailpin
$ cd django.admin.auth.emailpin
$ make setup PYTHON_BIN=/path/to/python3
$ make tests
```
