from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        print('POST')
        data = json.loads(request.body)
        print(data)
        return HttpResponse(data)

