from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("users:login")
    return redirect("flights:index")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username , password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("flights:index"))
        else:
            return render(request,"users/login.html",{
                "message":"invalid credentials."
            })
    return render(request,"users/login.html")
def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "message" : "logged out."
    })

def register(request):
    pass