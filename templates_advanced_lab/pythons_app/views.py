from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from pythons_core.view_mixins import GroupRequiredMixin
from .forms import PythonCreateForm, FilterForm
from .models import Python

from pythons_core.decorators import group_required


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }
    # index?page=3&page_size=10


# def index(request):
#     params = extract_filter_values(request.GET)
#     order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
#     pythons = Python.objects.filter(name__icontains=params['text']).order_by(order_by)
#
#     for python in pythons:
#         python.can_delete = python.created_by_id == request.user.id
#
#     context = {
#         'pythons': pythons,
#         'current_page': 'home',
#         'filter_form': FilterForm(initial=params),
#         # 'categories': PythonCategory.objects.all(),
#     }
#
#     return render(request, 'index.html', context)

class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    order_by_asc = True
    order_by = 'name'
    contains_text = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        # self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'name' if self.order_by == FilterForm.ORDER_ASC else '-name'
        result = self.model.objects.filter(name__icontains=self.contains_text).order_by(order_by)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            'order': self.order_by,
            'text': self.contains_text
        })

        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pythons'] = sorted(context['pythons'], key=lambda x: x.name, reverse=not self.order_by_asc)
    #     context['filter_form'] = FilterForm(initial={'order': self.order_by_asc})
    #     return context


def python_details(request, pk, slug=None):
    python = Python.objects.get(pk=pk)
    if slug and python.name.lower() != slug.lower():
        return redirect('404')
    context = {
        'python': python,
    }

    return render(request, 'pythons/details.html', context)


# @group_required(groups=['Regular User'])
# @login_required
# def create(req):
#     if req.method == 'GET':
#         context = {
#             'form': PythonCreateForm(),
#             'current_page': 'create',
#         }
#
#         return render(req, 'create.html', context)
#     else:
#         form = PythonCreateForm(req.POST, req.FILES)
#         print(form)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         context = {
#             'form': form,
#             'current_page': 'create',
#         }
#
#         return render(req, 'create.html', context)

# @method_decorator(group_required(groups=['Regular User']), name='dispatch')
class PythonCreateView(GroupRequiredMixin, LoginRequiredMixin, FormView):
    form_class = PythonCreateForm
    template_name = 'create.html'
    success_url = reverse_lazy('index')
    groups = ['User']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
