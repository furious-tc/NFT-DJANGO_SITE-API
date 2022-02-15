from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    path('about/', about, name='about'),
    path('auth/', about, name='auth'),
    path('registration/', about, name='registration'),

]



