"""Models definition."""
import random
from django.db import models
from django.core.mail import send_mail


class User(models.Model):
    """Registered user."""

    max_email_length = 200
    title_fld_name = "Login"
    title_fld_email = "Custom email"
    title_fld_active = "Active"

    name = models.CharField(verbose_name=title_fld_name, max_length=max_email_length)
    custom_email = models.EmailField(verbose_name=title_fld_email, blank=True, default='')
    is_active = models.BooleanField(verbose_name=title_fld_active, default=True)

    class Meta:
        """This class is abstract."""

        abstract = True

    def __str__(self):
        """String representation."""
        return self.name


class PinCode(models.Model):
    """PIN code for auth."""

    user_name = models.CharField(max_length=User.max_email_length)
    sent_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=6)

    class Meta:
        """This class is abstract."""

        abstract = True
        verbose_name = "PIN code"
        verbose_name_plural = "PIN codes"

    def __str__(self):
        """String representation."""
        return "{}: {}".format(self.user_name, self.code)

    @classmethod
    def superuser_email(cls):
        """Child class must return DB superuser email as string."""
        raise NotImplementedError("{}.superuser_email".format(cls.__class__.__name__))

    @classmethod
    def mail_inacive(cls, user):
        """Child class must return from, subj and body for mail to disabled user."""
        raise NotImplementedError("{}.mail_inacive({})".format(cls.__class__.__name__, user))

    @classmethod
    def mail_login(cls, user, pin):
        """Child class must return from, subj and body for mail with pin to login."""
        raise NotImplementedError("{}.mail_login({}, {})".format(cls.__class__.__name__, user, pin))

    @classmethod
    def create(cls, username):
        """Return random PIN code."""
        return cls(
          user_name=username,
          code=''.join(random.sample([str(i) for i in range(10)] * 4, 6))
        )

    @classmethod
    def auth(cls, user_class, username):
        """Start auth user."""
        users = user_class.objects.filter(name=username)
        if not users:
            return False

        user = users[0]
        mail_list = []
        if user.name == 'admin':
            mail_list.append(cls.superuser_email())
        else:
            mail_list.append(user.name)

        if user.custom_email:
            mail_list.append(user.custom_email)

        if not user.is_active:
            fld_from, fld_subj, fld_body = cls.mail_inacive(user)
            send_mail(fld_subj, fld_body, fld_from, mail_list, fail_silently=False)
            return False

        codes = cls.objects.filter(user_name=username)
        if codes:
            code = codes[0]
        else:
            code = cls.create(username)
            code.save()

        fld_from, fld_subj, fld_body = cls.mail_login(user, code)
        send_mail(fld_subj, fld_body, fld_from, mail_list, fail_silently=False)

        return True

    @classmethod
    def is_valid(cls, username, pincode):
        """Return True if given poin valid for user."""
        pins = cls.objects.filter(user_name=username)

        if not pins:
            return False

        if pins[0].code != pincode:
            return False

        for i in pins:
            i.delete()

        return True
