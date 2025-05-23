from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()  # Получаем все задачи
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем задачу
            return redirect('todo_list')  # Перенаправляем на список задач
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # После редактирования перенаправляем на главную страницу
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form})

