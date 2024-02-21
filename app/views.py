from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
import json
from .models import customUser


# Create your views here.

# Creating user from data recieved as json
@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        # We are hitting api by postman so we got data in request.body as json
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')

        if (name and email and phone and password):
            try:
                user = customUser(name=name, email=email, phone=phone, password=password)
                user.save()
                return JsonResponse({'message': f"User created with Id: {user.id}"})
            except:
                return JsonResponse('Failed to register!!')

        return HttpResponse('Failed to register!!')

