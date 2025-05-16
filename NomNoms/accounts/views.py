from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm

# Create your views here.

def all_accounts(request):
    return HttpResponse('returning accounts')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CustomUserCreationForm()
        
        return render(request, 'register.html', {'form': form})