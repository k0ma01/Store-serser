from django.contrib import auth,messages
from django.contrib.auth import get_user_model
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.views import LoginView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm


class UserRegistrationView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context=super(UserRegistrationView,self).get_context_data()
        context['title']='Store-Регистрация'
        return context


# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)


class UserProfileView(UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')
    extra_context = {'title': 'Store - Личный Кабинет'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context

    def get_object(self, queryset=None):
        return self.request.user


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user ,data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Поздравляем! Вы успешно зарегестрировались! ')
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#            form = UserProfileForm(instance=request.user)
#
#     context = {'title': 'Store - Профиль',
#                'form': form,
#                'baskets':Basket.objects.filter(user=request.user),
#                }
#     return render(request, 'users/profile.html', context)
#

