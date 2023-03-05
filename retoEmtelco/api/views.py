from django.shortcuts import render

# from django.http import JsonResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Vulnerability
# Se importa para poder hacer peticiones a otros servidores
import requests
# import json para poder transformar lo que llega en los request
import json


class VulnerabilityView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        # response = requests.get(
        #     "https://services.nvd.nist.gov/rest/json/cves/2.0")
        # data = response.json()
        # vulnerabilities = list(Vulnerability.objects.values())

        # for vuln_data in data['vulnerabilities']:
        #     for vul in vulnerabilities:
        #         if (vuln_data['cve']['id'] != vul['vuln_id']):
        #             print('hello')
        #             datos = {'message': 'Success',
        #                      'vulnerabilities': vulnerabilities}
        #     vuln_id = vuln_data['cve']['id']
        #     description = vuln_data['cve']['descriptions'][0]['value']
        #     # severity = vuln_data['cve']['metrics']['cvssMetricV2'][0]['baseSeverity']
        #     severity = 'HIGH'
        #     vulnerability = Vulnerability(
        #         vuln_id=vuln_id, description=description, severity=severity)
        #     vulnerability.save()

        if (id > 0):
            vulnerabilities = list(
                Vulnerability.objects.filter(id=id).values())
            if len(vulnerabilities) > 0:
                vulnerability = vulnerabilities[0]
                data = {'message': 'Success',
                        'vulnerabilities': vulnerability}
            else:
                data = {'message': 'Vulnerability not found....'}
            return JsonResponse(data)
        else:
            vulnerabilities = list(Vulnerability.objects.values())
            if len(vulnerabilities) > 0:
                data = {'message': 'Success',
                        'vulnerabilities': vulnerabilities}
            else:
                data = {'message': 'Vulnerabilities not found....'}

        return JsonResponse(data)

    def post(self, request):
        jd = json.loads(request.body)
        Vulnerability.objects.create(
            vuln_id=jd['vuln_id'], description=jd['description'], severity=jd['severity'])
        data = {'message': 'Success', 'vulnerability': jd}
        return JsonResponse(data)

    def put(self, request, id):

        jd = json.loads(request.body)
        vunerabilities = list(Vulnerability.objects.filter(id=id).values())
        if len(vunerabilities) > 0:
            vulnerability = Vulnerability.objects.get(id=id)
            vulnerability.vuln_id = jd['vuln_id']
            vulnerability.description = jd['description']
            vulnerability.severity = jd['severity']
            vulnerability.save()
            data = {'message': 'Success', 'vunerability': jd}
        else:
            data = {'message': 'Success', 'vunerability': jd}
        return JsonResponse(data)

    def delete(self, request, id):
        vunerabilities = list(Vulnerability.objects.filter(id=id).values())
        if len(vunerabilities) > 0:
            Vulnerability.objects.filter(id=id).delete()
            data = {'message': 'Success'}
        else:
            data = {'message': 'Success'}
        return JsonResponse(data)
