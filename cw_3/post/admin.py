from django.contrib import admin
from .models import Thread, Post

admin.site.register(Thread)
admin.site.register(Post)

# Настройка маршрутов (cw_3/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
]

# Register your models here.
