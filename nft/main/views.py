import json
import re

import requests
from django.http.response import HttpResponseNotFound, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import get_template
from .models import *
from .generator import filters

data = Cards.objects.all()

menu = [
    {"title": "HOME", "url_active": "home"},
    {"title": "SHOP", "url_active": "shop"},
    {"title": "ABOUT", "url_active": "about"},
]


def index(request):
    context = {
        "data": data,
        "menu": menu,
        "page": "home",
    }
    return render(request, 'main/index.html', context)


def shop(request):

    if request.GET == {}:
        url = 'https://api.x.immutable.com/v1/orders?include_fees=true&status=active&sell_token_address=0xac98d8d1bb27a94e79fbf49198210240688bb1ed&sell_metadata={"Attribute":["Accountability","Ambition","Conviction","Curiosity","Empathy","Gratitude","Humility","Kind Candor","Kindness","Optimism","Patience","Self-awareness","Tenacity","Special"],"Spectacular":["Bubble Gum","Diamond","Gold","Hologram","Lava"],"Token Frame":["Black","Caviar","Champagne","Clear","Emerald","Fur","Galaxy","Gold","Granite","Marble","Neon","Pearl","Rainbow","Silver","Wood"]}&buy_token_type=ETH&page_size=30&cursor='
        print(url)
    else:
        try:
            print(request.GET)
            url = filters(request.GET)
            print(f'{url} \ngood')
            data = requests.get(url.replace('\n', '')).json()
            prices = []
            for i, c in enumerate(data["result"]):
                data_price = c['buy']['data']['quantity']
                if len(data_price) == 18:
                    price = f'0.{round(int(data_price[:5]), 3)}'
                elif len(data_price) == 19:
                    first_num = data_price[0]
                    price = f'{first_num}.{int(data_price[1:6])}'
                elif len(data_price) == 20:
                    first_num = data_price[:2]
                    price = f'{first_num}.{int(data_price[2:7])}'
                elif len(data_price) == 21:
                    first_num = data_price[:3]
                    price = f'{first_num}.{int(data_price[3:8])}'
                else:
                    continue
                data["result"][i]["buy"]["data"]["price"] = price
                print(data)
            print(data)


            context = {
                "data": data,
                "menu": menu,
                "page": "shop",


            }

            return render(request, 'main/shop.html', context)
        except AttributeError:
            url = 'https://api.x.immutable.com/v1/orders?include_fees=true&status=active&sell_token_address=0xac98d8d1bb27a94e79fbf49198210240688bb1ed&sell_metadata={"Attribute":["Accountability","Ambition","Conviction","Curiosity","Empathy","Gratitude","Humility","Kind Candor","Kindness","Optimism","Patience","Self-awareness","Tenacity","Special"],"Spectacular":["Bubble Gum","Diamond","Gold","Hologram","Lava"],"Token Frame":["Black","Caviar","Champagne","Clear","Emerald","Fur","Galaxy","Gold","Granite","Marble","Neon","Pearl","Rainbow","Silver","Wood"]}&buy_token_type=ETH&page_size=30&cursor='
        except IndexError:
            url = 'https://api.x.immutable.com/v1/orders?include_fees=true&status=active&sell_token_address=0xac98d8d1bb27a94e79fbf49198210240688bb1ed&sell_metadata={"Attribute":["Accountability","Ambition","Conviction","Curiosity","Empathy","Gratitude","Humility","Kind Candor","Kindness","Optimism","Patience","Self-awareness","Tenacity","Special"],"Spectacular":["Bubble Gum","Diamond","Gold","Hologram","Lava"],"Token Frame":["Black","Caviar","Champagne","Clear","Emerald","Fur","Galaxy","Gold","Granite","Marble","Neon","Pearl","Rainbow","Silver","Wood"]}&buy_token_type=ETH&page_size=30&cursor='

    data = requests.get(url).json()

    context = {
        "data": data,
        "menu": menu,
        "page": "shop",

    }
    return render(request, 'main/shop.html', context)


def about(request):
    context = {
        "data": data,
        "menu": menu,
        "page": "about",
    }
    return render(request, 'main/about.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')




