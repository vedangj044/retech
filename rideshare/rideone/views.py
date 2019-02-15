from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
xe
from rideone.forms import VehicleForm, rideForm
from django import forms



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
# Create your views here.
@login_required(login_url="/signup")
def home(request):
    username = request.user.id
    v = vehicle.objects.filter(user=username)
    listofv = v
    if request.method == "POST":
        MyVehicle1 = rideForm(request.POST)
        if MyVehicle1.is_valid():
            to = MyVehicle1.cleaned_data['to']
            fro = MyVehicle1.cleaned_data['fro']
            date = MyVehicle1.cleaned_data['date']
            time = MyVehicle1.cleaned_data['time']
            vehicl = MyVehicle1.cleaned_data['widget']
            add1 = ride(to=to, user=request.user, fro=fro, contact_date=date, contact_time=time)
            getvehicle = vehicle.object.get(name=vehicl)
            add1.vehicle = getvehicle
            add1.save()
            print(add1)
    else:
        MyVehicle1 = rideForm()

    return render(request, 'home.html', {'vehicle': v})

@login_required(login_url="/signup")
def new(request):
    username = request.user.id
    v = vehicle.objects.filter(user=username)
    listofv = v
    if request.method == "POST":
        MyVehicle = VehicleForm(request.POST)
        if MyVehicle.is_valid():
            name = MyVehicle.cleaned_data['name']
            register = MyVehicle.cleaned_data['register']
            people = MyVehicle.cleaned_data['people']
            model1 = MyVehicle.cleaned_data['model']
            add = vehicle(name=name, user=request.user, register=register, people=people, model=model1)
            add.save()
    else:
        MyVehicle = VehicleForm()
    return render(request, 'new.html')
