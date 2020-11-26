from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View, TemplateView

from resources.models import Pet


class IndexView(View):
    def get(self, request):
        context = {
            'heading_text': 'Hello from View',
            'pets': Pet.objects.all(),
        }

        return render(request, 'cbv/index.html', context)

    def post(self, request):
        pass


class IndexTemplateView(TemplateView):
    template_name = 'cbv/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['heading_text'] = 'Hello from TemplateView'
        context['pets'] = Pet.objects.all()

        return context


class PetsListView(ListView):
    template_name = 'cbv/index.html'
    model = Pet
    context_object_name = 'pets'
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        if 'page_size' in request.GET:
            self.paginate_by = request.GET['page_size']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['heading_text'] = 'Pets list'

        return context


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'cbv/details.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context['pet']

        context['heading_text'] = f'{pet.name}\'s details'

        return context


class PetCreateView(CreateView):
    model = Pet
    template_name = 'cbv/create-pet.html'
    fields = '__all__'
    success_url = reverse_lazy('cbv pets list')
