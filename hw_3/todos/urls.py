from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:id>/delete/', views.todo_delete, name='todo_delete'),
    path('<int:id>/edit/', views.todo_edit, name='todo_edit'),  # Новый маршрут для редактирования
]