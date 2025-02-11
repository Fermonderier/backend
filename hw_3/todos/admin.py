from django.contrib import admin
from .models import Todo

admin.site.register(Todo)

# Настройка маршрутов (hw_3/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
]