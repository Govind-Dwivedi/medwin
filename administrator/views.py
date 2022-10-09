from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def admin_home(request):
    if request.user.is_administrator == True:
        return render(request, 'admin_home.html')
    else:
        return redirect('loginUser')

# Create your views here.
