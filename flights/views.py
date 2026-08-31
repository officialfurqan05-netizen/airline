from django.shortcuts import render ,get_object_or_404
from django.urls import reverse
from .models import Flight ,Passenger
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="users:login")
def index(request):
    context ={
        "flights" : Flight.objects.all()
    }
    return render(request,"flights/index.html",context)
@login_required(login_url="users:login")
def flight(request,flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    context = {
        "flight" : flight,
        "passengers": flight.passengers.all(),
        "non_passengers":Passenger.objects.exclude(flights=flight).all()
    }
    return render(request,"flights/flight.html",context)
@login_required(login_url="users:login")
def book(request,flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight",args=(flight.id,)))