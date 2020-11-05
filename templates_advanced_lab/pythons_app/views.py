from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(req):
    pythons = Python.objects.all()
    context = {
        'pythons': pythons,
        'current_page': 'home',
    }

    return render(req, 'index.html', context)


def create(req):
    if req.method == 'GET':
        context = {
            'form': PythonCreateForm(),
            'current_page': 'create',
        }

        return render(req, 'create.html', context)
    else:
        data = req.POST
        form = PythonCreateForm(data)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
