from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from pythons_auth.forms import RegisterForm, ProfileForm, LoginForm


# @transaction.atomic
# def register_user(request):
#     if request.method == 'GET':
#         context = {
#             'user_form': RegisterForm(),
#             'profile_form': ProfileForm(),
#         }
#
#         return render(request, 'auth/register.html', context)
#     else:
#         user_form = RegisterForm(request.POST)
#         profile_form = ProfileForm(request.POST, request.FILES)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#
#             login(request, user)
#             return redirect('index')
#
#         context = {
#             'user_form': RegisterForm(),
#             'profile_form': ProfileForm(),
#         }
#
#         return render(request, 'auth/register.html', context)

# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'auth/register.html'
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['user_form'] = context['form']
#         context['profile_form'] = ProfileForm()
#
#         return context
class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = RegisterForm()
        context['profile_form'] = ProfileForm()
        return context

    @transaction.atomic
    def post(self, request):
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('index')

        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }

        return render(request, 'auth/register.html', context)


def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'index'


def login_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }

        return render(request, 'auth/login.html', context)
    else:
        login_form = LoginForm(request.POST)

        return_url = get_redirect_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect(return_url)

        context = {
            'login_form': login_form,
        }

        return render(request, 'auth/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('index')
