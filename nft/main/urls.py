from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
]



