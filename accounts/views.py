from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from mdas.models import Mda
from capitals.models import Capital
from overheads.models import Overhead
from revenues.models import Revenue
from personnels.models import Personnels


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    mda_view = Mda.objects.all()
    context = {
        'mdas': mda_view
    }
    return render(request, 'accounts/dashboard.html', context)
