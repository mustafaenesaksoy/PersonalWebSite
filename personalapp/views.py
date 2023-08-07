from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.urls import reverse
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request,"personalapp/index.html")

def contact(request):
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        models.User.objects.create(name = name,email = email,message = message)
        messages.success(request, 'Mesajınız iletildi!')
        return redirect(reverse("personalapp:index"))
    else:
        return render(request, "personalapp/contact.html")