import os
import re
import urllib
from os.path import join, isfile

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from resources.forms import PetForm
from resources.models import Pet


def pets(request):
    if request.method == 'GET':
        pets = Pet.objects.all()

        context = {
            'pets': pets,
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


def fix_path(path):
    path = urllib.parse.unquote(path)
    wrong_separator = '/'
    correct_separator = os.path.sep
    result = []
    for x in path:
        if x == wrong_separator:
            result.append(correct_separator)
        else:
            result.append(x)

    return ''.join(result)


def get_public_file(request, path_to_file):
    full_path = fix_path(join(settings.MEDIA_ROOT, 'public', path_to_file[len('/media/public/'):]))
    print(full_path)
    if isfile(full_path):
        has_access = True

        if has_access:
            file = open(full_path, 'rb')
            response = HttpResponse(content=file)
            response['Content-Dispostion'] = 'attachment'
            return response

    return None
