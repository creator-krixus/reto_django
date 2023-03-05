from django.db import models


class Vulnerability(models.Model):
    vuln_id = models.CharField(max_length=50)
    description = models.TextField()
    severity = models.CharField(max_length=20)
