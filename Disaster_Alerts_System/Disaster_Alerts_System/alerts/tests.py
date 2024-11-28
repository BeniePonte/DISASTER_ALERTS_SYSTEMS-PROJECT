from django.test import TestCase
from .models import DisasterAlert

class DisasterAlertTestCase(TestCase):
    def test_create_alert(self):
        alert = DisasterAlert.objects.create(
            type="flood",
            location="Paris",
            severity=3,
            description="Flooding due to heavy rain."
        )
        self.assertEqual(str(alert), "flood at Paris (Severity: 3)")