from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from pythons_core.decorators import group_required
from .forms import PythonCreateForm
from .models import Python


def index(req):
    pythons = Python.objects.all()
    context = {
        'pythons': pythons,
        'current_page': 'home',
        # 'categories': PythonCategory.objects.all(),
    }

    return render(req, 'index.html', context)

# @login_required(login_url='login user')
@group_required(groups=['Regular User'])
def create(req):
    if req.method == 'GET':
        context = {
            'form': PythonCreateForm(),
            'current_page': 'create',
        }

        return render(req, 'create.html', context)
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
