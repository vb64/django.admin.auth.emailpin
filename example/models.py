"""Models definition."""
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_admin_auth_emailpin.models import User


class OrgUser(User):

    title_fld_name = _("Login")
    title_fld_email = _("Custom email")
    title_fld_active = _("Active")

    is_admin = models.BooleanField(verbose_name=_("Admin"), default=False)

    class Meta:
        verbose_name = _("Org user")
        verbose_name_plural = _("Org users")
