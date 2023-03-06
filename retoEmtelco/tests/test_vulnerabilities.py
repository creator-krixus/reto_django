import pytest

from api.models import Vulnerability
from django.test import TestCase


@pytest.mark.django_db
class CreateVulnerabilityTestCase(TestCase):
    def test_creation_vulnerabilities(self):
        vulnerability = Vulnerability.objects.create(
            vuln_id='CVE-2000-0454',
            description='asdsadsa',
            severity='LOW'
        )
        vulnerability = Vulnerability.objects.get(pk=vulnerability.pk)
        self.assertEqual(vulnerability.vuln_id, 'CVE-2000-0454')
        self.assertEqual(vulnerability.description, 'asdsadsa')
        self.assertEqual(vulnerability.severity, 'LOW')


@pytest.mark.django_db
class TestCreationVunerabilityInDataBaseFail(TestCase):
    def test_creation_vulnerability_fail(self):
        vulnerability = Vulnerability.objects.create(
            vuln_id='CVE-2000-0454',
            description='asdsadsa',
        )
        vulnerability.save()
        self.assertIsNone(Vulnerability.objects.filter(id=8).first())


class ViewsTest(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 404)


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get(
            'http://127.0.0.1:8000/api/v1/vulnerability/')
        self.assertEqual(response.status_code, 200)
