import uuid
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import auth

import json

from .models import Article, User

# Create your views here.


def articlelist(request):
    userid = 1
    article_list = list(Article.objects.filter(userid = userid).values())
    return JsonResponse(article_list, safe=False)

def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username", "")
        password = data.get("password", "")

        if username == 'harry' and password == "panchuang001":
            request.session['islogin'] = True
            request.session['user_name'] = username

            return JsonResponse({"login": "true"})
    request.session['islogin'] = False
    return JsonResponse({"login": "false"})

def register(request):
    if request.methood == "POST":
        data = json.loads(request.body)

        username = data.get("username", "")
        password = data.get("password", "")
        email = data.get("email", "")

        user = AuthUser()

        user.username = username
        user.password = user
        user.email = email
        user.save()

        




