

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth import authenticate, login




from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model


def index(request):
    return render(request,'template/template.html',{})   



@csrf_exempt
def verify_user(request):
    chat_id= request.POST.get('chat_id')
    text = request.POST.get('text')
    print(request.POST,chat_id)
    print(users.objects.values_list('telegram_id',flat=True))

    usernm = None

    if users.objects.filter(telegram_id=chat_id).exists():
        user = users.objects.get(telegram_id=chat_id)
        print(user)
        result = 'registerd'
        user1 = User.objects.get(id=user.uid_id)
        usernm= user1.username
    else :
        print('not_authenticated')
        result = 'not_registered'


    response = {
        'response': result,
        'username': usernm
    }
    return JsonResponse(response)



@csrf_exempt
def  loginuser(request):
    chat_id= request.POST.get('chat_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    print('+++++++++pass++++++++',password)
    user = authenticate_user(username=username, password=password)
    username = user.username

    if user is not None:
        profile = users.objects.get(uid_id=user.id)
        profile.telegram_id = chat_id
        profile.save()
        result ={
            "status":"authenticated",
            "message": "login sucessfull",
            "username" : username
        }
        return JsonResponse(result)
    else:
        result ={
            "status":"not_authenticated",
            "message": "Invalid username or password.",
        }
        return JsonResponse(result)





def authenticate_user(username, password):
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            return user
    except User.DoesNotExist:
        pass
    return None

@csrf_exempt
def logout_user(request):
    chat_id= request.POST.get('chat_id')
    try:
        user = users.objects.get(telegram_id=chat_id)
        user.telegram_id = None
        user.save()
        result = {
            'result':'logout_success'
        }
    except users.DoesNotExist:
        result = {
            'result':'not_logged_in'
            }

    return JsonResponse(result)

@csrf_exempt
def register_user(request):
    chat_id= request.POST.get('chat_id')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = User.objects.create_user(username,email,password)
        print("=======password========",password)
        print('======uid====ffff=',user.id)
        tele = users.objects.create(uid=user)
        result={
            'resp':'registred'
        }
    except:
        result = {
            'resp':'not_registred'
            }

    return JsonResponse(result)




