from os.path import join, isfile

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from resources.forms import PetForm
from resources.models import Pet


def pets(request):
    if request.method == 'GET':
        context = {
            'pets': Pet.objects.all(),
            'form': PetForm(),
        }

        return render(request, 'resources/pets_index.html', context)
    else:
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('pets')

        context = {
            'pets': Pet.objects.all(),
            'form': form,
        }

        return render(request, 'resources/pets_index.html', context)


def get_private_file(request, path_to_file):
    full_path = join(settings.MEDIA_ROOT, 'private', path_to_file[len('/media/private/'):])
    if isfile(full_path):
        has_access = True

        if has_access:
            file = open(full_path, 'rb')
            response = HttpResponse(content=file)
            response['Content-Dispostion'] = 'attachment'
            return response

    return None
