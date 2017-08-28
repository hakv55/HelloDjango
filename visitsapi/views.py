from django.shortcuts import render
from visitsapi.forms import VisitsForm
from django.http import JsonResponse
from rest_framework import status
from django.core import serializers
import json
# Create your views here.



def add_visit(request):
    visit_form = VisitsForm(request.post)
    is_valid = visit_form.is_valid()
    if not is_valid:
        response = JsonResponse({"errors": visit_form.errors.get_json_data()})
        response.status_code = status.HTTP_400_BAD_REQUEST
    else:
        visit = visit_form.save()
        data = serializers.serialize("json", [visit, ])
        response = JsonResponse(json.loads(data))
        response.status_code = status.HTTP_201_CREATED
    return response


