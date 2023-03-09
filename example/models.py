"""Models definition."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_admin_auth_emailpin.models import User, PinCode


class OrgUser(User):
    title_fld_name = _("Login")
    title_fld_email = _("Custom email")
    title_fld_active = _("Active")

    is_admin = models.BooleanField(verbose_name=_("Admin"), default=False)

    class Meta:
        verbose_name = _("Org user")
        verbose_name_plural = _("Org users")


class Pin(PinCode):
    email_from = 'noreply@example.com'

    @classmethod
    def mail_secrets(cls):
        """Return DB superuser email, SMTP login and password."""
        return (
          'admin@example.com',
          'example.admin@gmail.com',
          'smtp-password',
        )

    @classmethod
    def mail_inacive(cls, user):
        return (
          cls.email_from,
          _("Your login at example.com was disabled."),
          _("Your account {} is disabled. Ask for admin to solve issue.").format(user),
        )

    @classmethod
    def mail_login(cls, user, pin):
        return (
          cls.email_from,
          _("Login to example.com"),
          _("To login as {} use PIN code: {}").format(user, pin.code),
        )
