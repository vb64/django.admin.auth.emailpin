"""Models definition."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    """Registered user."""

    name = models.CharField(verbose_name=_("Login"), max_length=20)
    custom_email = models.EmailField(verbose_name=_("Custom email"), blank=True)

    def __str__(self):
        """String representation."""
        return self.name


class PinCode(models.Model):
    """PIN code for auth."""

    user_name = models.CharField(max_length=200)
    sent_date = models.DateTimeField('date sent')
    code = models.CharField(max_length=6)

    class Meta:
        # ordering = ['du']
        verbose_name = _("PIN code")
        verbose_name_plural = _("PIN codes")

    def __str__(self):
        """String representation."""
        return "{}: {}".format(self.user_name, self.code)
