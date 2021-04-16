from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from loginstuff.models import Therapist

def home(request):
    return render(request, 'index.html', {})