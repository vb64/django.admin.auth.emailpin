"""Test GeoItem class.

make test T=test_models.py
"""
# import pytest
from . import TestBase


class TestsModels(TestBase):
    """library models."""

    @staticmethod
    def test_user():
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
