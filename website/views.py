from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Records
# Create your views here.


def home(request):
    recordss= Records.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in ')
            return redirect('home')
        else:
            messages.success(request, 'There was some error while login in')
            return redirect('home')
    else:
        return render(request, 'home.html', {'recordss':recordss })


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out Successfully')
    return redirect('home')





def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html', {'form': form})

    return render(request, 'register.html', {'form':form})



def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record= Records.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect('home')

