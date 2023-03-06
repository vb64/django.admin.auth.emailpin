"""Models definition."""
import random

from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    """Registered user."""

    max_email_length = 200

    name = models.CharField(verbose_name=_("Login"), max_length=max_email_length)
    custom_email = models.EmailField(verbose_name=_("Custom email"), blank=True)
    is_active = models.BooleanField(verbose_name=_("Active"), default=True)

    def __str__(self):
        """String representation."""
        return self.name


class PinCode(models.Model):
    """PIN code for auth."""

    user_name = models.CharField(max_length=User.max_email_length)
    sent_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=6)

    class Meta:
        # ordering = ['du']
        verbose_name = _("PIN code")
        verbose_name_plural = _("PIN codes")

    def __str__(self):
        """String representation."""
        return "{}: {}".format(self.user_name, self.code)

    @classmethod
    def create(cls, username):
        """Return random PIN code."""
        return cls(
          user_name=username,
          code=''.join(random.sample([str(i) for i in range(10)] * 4, 6))
        )
