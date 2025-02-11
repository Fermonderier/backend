# hw_3/views.py
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('thread_list')
