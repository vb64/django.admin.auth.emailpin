"""Models definition."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_admin_auth_emailpin import User


class OrgUser(User):

    is_admin = models.BooleanField(verbose_name=_("Admin"), default=False)

    class Meta:
        verbose_name = _("Org user")
        verbose_name_plural = _("Org users")
