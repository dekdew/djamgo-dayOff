from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from dayOff.forms import DayOffModelForm
from dayOff.models import DayOff


def is_staff(user):
  return user.groups.filter(name='staff').exists()


def is_manager(user):
  return user.groups.filter(name='manager').exists()


def my_login(request):
  context = {}

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user:
      login(request, user)

      next_url = request.POST.get('next_url')
      if next_url:
        return redirect(next_url)
      else:
        if is_manager(user):
          return redirect('/admin/dayOff/dayoff/')
        elif is_staff(user):
          return redirect('index')
        else:
          return redirect('index')
    else:
      context['username'] = username
      context['password'] = password
      context['error'] = 'Wrong username or password!'

  next_url = request.GET.get('next')
  if next_url:
    context['next_url'] = next_url

  return render(request, 'dayOff/login.html', context=context)


def my_logout(request):
  logout(request)
  return redirect('login')


def my_register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('index')

  else:
    form = UserCreationForm()

  context = {'form': form}

  return render(request, 'dayOff/register.html', context=context)


@login_required
def index(request):
  dayOff_list = DayOff.objects.all()

  context = {
    'dayOff_list': dayOff_list
  }

  return render(request, template_name='dayOff/index.html', context=context)


@login_required
def newDayOff(request):
  context = {}
  if request.method == 'POST':
    form = DayOffModelForm(request.POST)
    if form.is_valid():
      new = form.save(commit=False)
      new.create_by = request.user
      new.save()
      return redirect('index')
  else:
    form = DayOffModelForm()

  context['form'] = form
  return render(request, 'dayOff/newDayOff.html', context=context)
