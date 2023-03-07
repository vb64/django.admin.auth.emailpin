"""Models definition."""
import random
from django.db import models


class User(models.Model):
    """Registered user."""

    max_email_length = 200
    title_fld_name = "Login"
    title_fld_email = "Custom email"
    title_fld_active = "Active"

    name = models.CharField(verbose_name=title_fld_name, max_length=max_email_length)
    custom_email = models.EmailField(verbose_name=title_fld_email, blank=True)
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
    def create(cls, username):
        """Return random PIN code."""
        return cls(
          user_name=username,
          code=''.join(random.sample([str(i) for i in range(10)] * 4, 6))
        )
