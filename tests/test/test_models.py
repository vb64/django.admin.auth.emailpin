"""Test GeoItem class.

make test T=test_models.py
"""
import pytest
from . import TestBase


class TestsModels(TestBase):
    """library models."""

    @staticmethod
    def test_orguser():
        """User model."""
        from example.models import OrgUser

        user = OrgUser(name='user@example.com', custom_email='')
        assert user.is_active
        assert str(user) == 'user@example.com'

    @staticmethod
    def test_pin():
        """Pin model."""
        from example.models import Pin

        pin = Pin.create('user@example.com')
        assert 'user@example.com: ' in str(pin)

    @staticmethod
    def test_base_pin():
        """PinCode model."""
        from django_admin_auth_emailpin.models import PinCode

        with pytest.raises(NotImplementedError) as err:
            PinCode.superuser_email()
        assert 'superuser_email' in str(err.value)

        with pytest.raises(NotImplementedError) as err:
            PinCode.mail_inacive(None)
        assert 'mail_inacive' in str(err.value)

        with pytest.raises(NotImplementedError) as err:
            PinCode.mail_login(None, None)
        assert 'mail_login' in str(err.value)

    def test_auth(self):
        """Method auth."""
        from example.models import Pin, OrgUser

        assert not Pin.auth(OrgUser, 'notexist')
        assert len(self.sended_emails) == 0

        user = OrgUser(name='user@example.com', custom_email='')
        user.save()

        assert Pin.auth(OrgUser, user.name)
        assert len(self.sended_emails) == 1

        self.sended_emails.clear()
        user.custom_email = 'private@mail.com'
        user.is_active = False
        user.save()

        assert not Pin.auth(OrgUser, user.name)
        assert len(self.sended_emails) == 1

        self.sended_emails.clear()
        user.is_active = True
        user.save()
        assert Pin.auth(OrgUser, user.name)
        assert len(self.sended_emails) == 1

        self.sended_emails.clear()
        user.name = 'admin'
        user.save()
        assert Pin.auth(OrgUser, user.name)
        assert len(self.sended_emails) == 1
        assert Pin.superuser_email() in self.sended_emails[-1][-2]
