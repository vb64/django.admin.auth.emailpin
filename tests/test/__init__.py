"""Root class for testing."""
from django.test import TestCase, Client


def mail_mock(sended_emails):
    """Return mock send_mail function."""
    def send_mail_mock(subj, body, mail_from, mail_to_list, fail_silently=False):
        """Mocked send_mail function."""
        sended_emails.append((subj, body, mail_from, mail_to_list, fail_silently))
        print("# send_mail:", '\n'.join([repr(i) for i in sended_emails[-1]]))

    return send_mail_mock


class TestBase(TestCase):
    """Base class for tests."""

    def setUp(self):
        """Set up Django client."""
        super().setUp()
        self.client = Client()

        from django_admin_auth_emailpin import models

        self.sended_emails = []
        self.send_mail_save = models.send_mail
        models.send_mail = mail_mock(self.sended_emails)

    def tearDown(self):
        """Clear tests."""
        from django_admin_auth_emailpin import models

        self.sended_emails.clear()
        models.send_mail = self.send_mail_save

        super().tearDown()
