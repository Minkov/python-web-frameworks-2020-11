from django.shortcuts import render

from templates_advanced.forms import TodoForm
from templates_advanced.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
        'state': True,
        'form': TodoForm,
    }

    return render(request, 'templates_advanced/index.html', context)
