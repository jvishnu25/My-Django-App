#from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Robin")

def login(request):
    return render(request,"login.html",{})
def logpage(request):
    return render(request,"logpage",{})
def home(request):
    return render(request,"home.html",{})