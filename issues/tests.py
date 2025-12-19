from django.test import TestCase
from django.contrib.auth.models import User
from .models import Issues


class IssueTestCase(TestCase):
    def test_issue_creation(self):
        user = User.objects.create(username = 'client')
        issue = Issues.objects.create(
            title = "Server Down",
            description = "Production server not responding",
            severity = "CRITICAL",
            created_by = user,

        )
        self.assertEqual(issue.status, "OPEN")
