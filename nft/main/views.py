import json
import re

import requests
from django.http.response import HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .models import *
from .generator import filters, response



menu = [
    {"title": "Home", "url_active": ""},
    {"title": "Shop", "url_active": "shop"},
    # {"title": "About", "url_active": "about"},
    {"title": "Account", "url_active": "account"},
]


def index(request):
    context = {

        "menu": menu,
        "page": "",
        "title": "Furious Django Project",
    }
    return render(request, 'main/index.html', context)


def shop(request):
    data = response(request)
    context = {
        "data": data,
        "menu": menu,
        "page": "shop",
        "title": "Shop listings",
    }

    return render(request, 'main/shop.html', context)


def about(request):
    context = {

        "menu": menu,
        "page": "about",
        "title": "About US",
    }
    return render(request, 'main/about.html', context)


def account(request):
    context = {

        "menu": menu,
        "page": "account",
        "title": "AUTH / REGISTRATION",
    }
    return render(request, 'main/account.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')




