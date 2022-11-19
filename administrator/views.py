from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from account.models import User
from patients.models import Patient, Appointment
from doctor.models import Doctor
from .forms import addDoctorForm


@permission_required("administrator.admin_things")
def admin_home(request):
    if request.user.is_administrator == True:
        return render(request, 'admin_home.html')
    else:
        return redirect('loginUser')


@permission_required("administrator.admin_things")
def patientsList(request):
    patients_list = User.objects.filter(is_patient=True).values()
    context = {'patientsList': patients_list, }
    return render(request, "patientslist.html", context)

@permission_required("administrator.admin_things")
def doctorsList(request):
    doctors = User.objects.filter(is_doctor=True).values()
    context = { 'doctors' : doctors, }
    return render(request, 'doclist.html', context)

@permission_required("administrator.admin_things")
def addDoctor(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get("email")
        fee = request.POST.get("fee")
        experience = request.POST.get("experience")

        if User.objects.filter(email=email).exists():
            u = User.objects.get(email=email)

            if u.is_doctor == False:
                u.is_doctor = True
                d = Doctor(user=u, experience=experience, consultFee=fee)       #Add new doctor
            else:
                d = Doctor.objects.get(user=u)
                d.experience = experience                                       #Update old doctor
                d.consultFee = fee

            u.save()
            d.save()
            return redirect('admin_home')
        else:
            context['remark'] = "This account do not exist. Enter another email."

    context['form'] = addDoctorForm()
    return render(request, 'add_doctor.html', context)


@permission_required("administrator.admin_things")
def removeDoc(request):
    remark = ''
    if request.method == 'POST':
        if User.objects.filter(email= request.POST.get('email')).exists():
            u = User.objects.get(email= request.POST.get('email'))
            if u.is_doctor == True:
                u.is_doctor = False
                u.save()
                d = Doctor.objects.get(user=u)
                apnts = Appointment.objects.filter(doctor=d)
                if apnts.exists():
                    for a in apnts:
                        a.delete()
                d.delete()
                p = Patient.objects.get(user=u)
                p.save()
                remark = "Task executed successfully, now given user is not a doctor"
            else:
                remark = "User is not a doctor"
        else:
            remark = "No such user exists"
    return render(request, 'removeDoc.html', {'remark' : remark})
    return render(request, 'appointment-history.html', context)

# Create your views here.
