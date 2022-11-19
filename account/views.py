from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from patients.models import Patient
from .models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        u = User(first_name=first_name, last_name=last_name, email=email, password=password)
        u.save()
        p = Patient(user=u)
        p.save()
        login(request, u)
        """
        form = UserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            p = Patient(user=u)
            p.save()
        """
        return redirect('patient_home')
    else:
       # form = UserCreationForm()
        #context = { 'form' : form }
        return render(request, "register.html")


def loginUser(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.is_authenticated:
                if user.is_administrator:
                    return redirect('admin_home')
                elif user.is_doctor:
                    return redirect('doc_home')
                else:
                    return redirect('patient_home')
        else:
            context['remark'] = "Either password do not match or user do not exist!"
    
    form = LoginForm()
    context['form'] = form
    return render(request, 'login.html', context)
    

def logoutUser(request):
    logout(request)
    return redirect('home')
# Create your views here.
