from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PythonCreateForm, FilterForm
from .models import Python


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }
    # index?page=3&page_size=10

def index(request):
    params = extract_filter_values(request.GET)
    order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
    pythons = Python.objects.filter(name__icontains=params['text']).order_by(order_by)

    for python in pythons:
        python.can_delete = python.created_by_id == request.user.id

    context = {
        'pythons': pythons,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
        # 'categories': PythonCategory.objects.all(),
    }

    return render(request, 'index.html', context)


def python_details(request, pk, slug=None):
    python = Python.objects.get(pk=pk)
    if slug and python.name.lower() != slug.lower():
        return redirect('404')
    context = {
        'python': python,
    }

    return render(request, 'pythons/details.html', context)


# @group_required(groups=['Regular User'])
@login_required
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
