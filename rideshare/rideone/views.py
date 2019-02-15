from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import main2
from rideone.models import vehicle, ride
from rideone.forms import VehicleForm, rideForm, search
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
        search1 = search(request.POST)
        print(MyVehicle1.errors)
        print(search1.errors)
        if MyVehicle1.is_valid():
            print(2)
            to = MyVehicle1.cleaned_data['to']
            fro = MyVehicle1.cleaned_data['fro']
            contact_date = MyVehicle1.cleaned_data['contact_date']
            contact_time = MyVehicle1.cleaned_data['contact_time']
            vehicl = MyVehicle1.cleaned_data['widget']
            add1 = ride(to=to, user=request.user, fro=fro, contact_date=contact_date, contact_time=contact_time)
            getvehicle = vehicle.objects.get(name=vehicl)
            add1.vehicl = getvehicle
            add1.save()
            print(add1)

        elif search1.is_valid():
            distance = {}
            to = search1.cleaned_data['to']
            fro = search1.cleaned_data['fro']
            contact_date = search1.cleaned_data['contact_date']
            for i in range(1, len(ride.objects.all())+1):
                print(i)
                available = ride.objects.get(id=i)
                f = open('rideone/find.txt', 'w+')
                f.write(" "+available.fro)
                f.write(" "+to)
                f.write(" "+fro)
                f.write(" "+available.to)
                f.close()
                c = main2.critical()
                distance[i]=c
            if distance:
                id1 = min(distance, key=distance.get)
                gf = ride.objects.get(id=id1)
                send = ["Vehicle: "+str(gf.vehicl), "Owner: "+str(gf.user)]
                return render(request, 'home.html/', {'send': send})
    else:
        MyVehicle1 = rideForm()

    return render(request, 'home.html', {'vehicle': v, 'form': MyVehicle1})

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
            return redirect('home')
    else:
        MyVehicle = VehicleForm()
    return render(request, 'new.html')
