from json import JSONDecodeError
import json
from django.views import View
from .models import Company
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.


class CompanyView(View):

    # metodo que se ejecuta cada vez que se envia una petición http
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        res = {}
        if (id > 0):
            result = list(Company.objects.filter(id=id).values())
            res = {
                "msg": "Sin resultados" if len(result) == 0 else "1 resultado",
                "result": {} if len(result) == 0 else result[0]
            }
        else:
            result = list(Company.objects.values())
            res = {
                "msg": str(len(result)) + " resultados" if len(result) > 1 else "1 resultado" if len(result) == 1 else "Sin resultados",
                "result": result
            }
        return JsonResponse(res)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        Company.objects.create(
            name=jd['name'], website=jd['website'], foundation=jd['foundation']
        )
        res = {
            "msg": "Registro exitoso"
        }
        return JsonResponse(res)

    def put(self, request, id):
        jd = json.loads(request.body)
        result = list(Company.objects.filter(id=id).values())
        if len(result) > 0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            res = {
                "msg": "Actualización exitosa"
            }
        else:
            res = {
                "msg": "Company not found"
            }
        return JsonResponse(res)

    def delete(self, request, id):
        result = list(Company.objects.filter(id=id).values())
        if len(result) > 0:
            Company.objects.filter(id=id).delete()
            res = {
                "msg": "Eliminación exitosa"
            }
        else:
            res = {
                "msg": "Company not found"
            }
        return JsonResponse(res)
