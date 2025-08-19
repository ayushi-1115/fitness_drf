from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from django.urls import reverse

class HealthTest(APITestCase):
    def test_health(self):
        url = reverse("health")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data.get("status"), "ok")
