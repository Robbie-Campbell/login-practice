from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from loginstuff.models import Therapist

def home(request):
    return render(request, 'index.html', {})

def insert_name(request):
    user = hasattr(request.user, "therapist")
    if user:
        return render(request, 'inputdata/insert_name.html', {})
    else:
        return HttpResponse("Sorry, You are not authorised to see this.")