from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def patient_home(request):
    return render(request, 'patient_home.html')
# Create your views here.
