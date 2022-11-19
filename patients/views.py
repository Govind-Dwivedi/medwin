from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import bookAppntFrom
from patients.models import Patient, Appointment
from doctor.models import Doctor

@login_required
def patient_home(request):
    return render(request, 'patient_home.html')

def book_Appointment(request):
    if request.method == 'POST':
        doc_id = int(request.POST.get("doctor_choice"))
        doc = Doctor.objects.get(id=doc_id)
        date = request.POST.get("date")
        time = request.POST.get("time")
        patient = Patient.objects.get(user = request.user)

        appointment = Appointment(patient=patient, doctor=doc, date=date, time=time)
        appointment.save()
        return redirect('patient_home')

    else:
        context = { 'form' : bookAppntFrom() }
        return render(request, 'book_Appointment.html', context)

def appointHistory(request):
    p = Patient.objects.get(user=request.user)
    context = {}
    if(Appointment.objects.filter(patient=p).exists()):
        appnts = Appointment.objects.filter(patient=p)
        appointments = []

        for a in appnts:
            doc_name = a.doctor.user.first_name + " " + a.doctor.user.last_name
            dict = {
                'doc_name' : doc_name,
                'fee' : a.doctor.consultFee,
                'date' : a.date,
                'time' : a.time,
                'comment' : a.doc_comment
            }
            appointments.append(dict)
        
        name = a.patient.user.first_name + " " + a.patient.user.last_name

        context = {
            'appointments' : appointments,
            'name' : name
        }
    return render(request, 'appointment-history.html', context)


# Create your views here.
