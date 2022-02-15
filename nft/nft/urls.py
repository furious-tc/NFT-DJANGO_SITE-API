from django.contrib import admin
from django.urls import path, include
from main.views import page_not_found
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

handler404 = page_not_found
