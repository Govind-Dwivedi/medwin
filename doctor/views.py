from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from patients.models import Appointment
from .models import Doctor

@permission_required("doctor.doctor_things")
def doc_home(request):
    if request.user.is_doctor == True:
        return render(request, 'doc_home.html')
    else:
        return redirect('loginUser')

@permission_required("doctor.doctor_things")
def appointHistory(request):
    d = Doctor.objects.get(user=request.user)
    context = {}
    if(Appointment.objects.filter(doctor=d).exists()):
        appnts = Appointment.objects.filter(doctor=d)
        appointments = []

        for a in appnts:
            pat_name = a.patient.user.first_name + " " + a.patient.user.last_name
            dict = {
                'id' : a.id,
                'pat_name' : pat_name,
                'email' : a.patient.user.email,
                'date' : a.date,
                'time' : a.time,
                'comment' : a.doc_comment
            }
            appointments.append(dict)
        
        name = a.doctor.user.first_name + " " + a.doctor.user.last_name
        context = {
            'appointments' : appointments,
            'name' : name
        }
    return render(request, 'appointHistory_doc.html', context)

@permission_required("doctor.doctor_things")
def doc_comment(request, id):
    if request.method == 'POST':
        com = request.POST.get("comment")
        a = Appointment.objects.get(id=id)
        a.doc_comment = com
        a.save()
        return redirect('appointHistory_doc')
    else:
        a = Appointment.objects.get(id=id)
        pat_name = a.patient.user.first_name + " " + a.patient.user.last_name
        appointment = {
            'pat_name' : pat_name,
            'email' : a.patient.user.email,
            'date' : a.date,
            'time' : a.time
        }
        context = {
            'appointment' : appointment,
            'id' : id
        }
        return render(request, 'doc_comment.html', context)

# Create your views here.
