from django import forms
from doctor.models import Doctor
from account.models import User

def giveChoices():
    options = []
    doctors = Doctor.objects.filter()
    for d in doctors:
        op = []
        u = User.objects.get(id = d.user_id)
        choice = u.first_name + " " + u.last_name + ", Exp-" + str(d.experience) + "yrs" + ", Fee - " + str(d.consultFee) + "Rs"
        op.append(str(d.id))
        op.append(choice)
        op = tuple(op)
        options.append(op)

    options = tuple(options)
    return options

class bookAppntFrom(forms.Form):
    doctor_choice = forms.ChoiceField(choices=giveChoices()) 
    date = forms.DateField()
    time = forms.TimeField()