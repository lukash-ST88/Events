from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView
from .models import CustomUser, Event


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'events/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile', user_id=self.request.user.pk)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'events/login.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'user_id': self.request.user.pk})


def logout_user(request):
    logout(request)
    return redirect('login_user')


def user_profile(request, user_id):
    events = Event.objects.all()
    user = CustomUser.objects.get(pk=user_id)
    context = {"user": user, 'events': events}
    return render(request, 'events/profile.html', context)


def user_profile_event(request, user_id, event_id):
    user = CustomUser.objects.get(pk=user_id)
    events = Event.objects.all()
    event = Event.objects.get(pk=event_id)
    context = {"user": user, 'events': events, 'event': event}
    return render(request, 'events/profile_event.html', context)


def add_user_to_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    user = request.user
    event.participants.add(user)
    return redirect('profile_event', user_id=user.id, event_id=event.id)


def remove_user_from_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    user = request.user
    event.participants.remove(user)
    return redirect('profile_event', user_id=user.id, event_id=event.id)


def main(request):
    return render(request, 'events/index.html')
