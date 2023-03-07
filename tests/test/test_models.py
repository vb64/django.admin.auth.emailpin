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
