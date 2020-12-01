from django.shortcuts import render


def handler400(request, exception):
    print(exception)
    return render(request, 'resources/pets_index.html')
