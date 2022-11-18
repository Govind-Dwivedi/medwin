from django import forms

class addDoctorForm(forms.Form):
    email = forms.EmailField()
    experience = forms.IntegerField()
    fee = forms.IntegerField()