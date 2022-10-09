from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def doc_home(request):
    if request.user.is_doctor == True:
        return render(request, 'doc_home.html')
    else:
        return redirect('loginUser')
# Create your views here.
