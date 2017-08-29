from django.shortcuts import render
from visitsapi.forms import VisitsForm
from django.http import JsonResponse
from rest_framework import status
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Visit
# Create your views here.


@csrf_exempt
def visits(request):

    if request.method == "POST":
        visit_form = VisitsForm(request.POST)
        is_valid = visit_form.is_valid()
        if not is_valid:
            response = JsonResponse({"errors": visit_form.errors})
            response.status_code = status.HTTP_400_BAD_REQUEST
        else:
            visit = visit_form.save()
            data = json.loads(serializers.serialize("json", [visit, ]))[0] # Model.objects?
            response_data = {'id': data['pk']}
            response_data.update(data['fields'])
            response = JsonResponse(response_data)
            response.status_code = status.HTTP_201_CREATED
        return response

    elif request.method == "GET":
        data = json.loads(serializers.serialize("json", Visit.objects.all()))  # Model.objects?
        response = JsonResponse(data, safe=False)
        response.status_code = status.HTTP_200_OK
        return response


