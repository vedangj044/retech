from django import forms

class VehicleForm(forms.Form):
   name = forms.CharField(max_length=30)
   register = forms.CharField(max_length=10)
   people = forms.CharField(max_length=10)
   model = forms.CharField(max_length=20)

class rideForm(forms.Form):
    to = forms.CharField(max_length=100)
    fro = forms.CharField(max_length=100)
    contact_date = forms.DateField()
    contact_time = forms.TimeField()
    #category = forms.ChoiceField(widget=forms.Select, choices=list)
    widget = forms.CharField(max_length=100)

class search(forms.Form):
    to = forms.CharField(max_length=100)
    fro = forms.CharField(max_length=100)
    contact_date = forms.DateField()
