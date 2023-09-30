from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.models import User
from django.contrib import auth
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from product.models import Basket
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView



class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(password=password, username=username)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    def get_context_data(self, **kwargs):
        context =  super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))
    def get_context_data(self, **kwargs):
        context =  super(UserProfileView, self).get_context_data()
        context['title'] = 'Store - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
    
#     context = {'title': 'Store - профиль',
#                'form': form,
#                'baskets': Basket.objects.filter(user=request.user),
#                }
#     return render(request, 'users/profile.html', context)

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/register.html', context)
