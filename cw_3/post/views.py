from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post

def redirect_to_threads(request):
    return redirect('thread_list')

def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def redirect_to_threads(request):
    return redirect('thread_list')

def thread_list(request):
    threads = Thread.objects.all()
    form = ThreadForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('thread_list')
    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    post_form = PostForm(request.POST or None, initial={'thread': thread})
    if request.method == "POST" and post_form.is_valid():
        post_form.save()
        return redirect('thread_detail', id=id)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'post_form': post_form})

def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    form = ThreadForm(request.POST or None, instance=thread)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('thread_detail', id=id)
    return render(request, 'post/thread_edit.html', {'form': form})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    
# Create your views here.

