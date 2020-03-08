from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        print('post')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('save')
            return render(request, 'user/register.html', {'form': form, 'message': 'register successful '})
    form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})


def validate_username(request):

    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
