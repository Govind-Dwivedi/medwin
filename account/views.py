from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from patients.models import Patient

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            p = Patient(user=u)
            p.save()
            return redirect('patient_home')
    else:
        form = UserCreationForm()
    context = { 'form' : form }
    return render(request, "register.html", context)


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
            context['remark'] = "User not found!";
    
    form = LoginForm()
    context['form'] = form
    return render(request, 'login.html', context)
    

def logoutUser(request):
    logout(request)
    return redirect('home')
# Create your views here.
