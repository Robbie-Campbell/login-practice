from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import PatientForm
from .models import Patient

def insert_patient(request):
    form = PatientForm
    if request.method == 'POST':
        form = PatientForm(request.POST) 
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PatientForm()
    return render(request, 'insert.html', {'form':form})

def list_patients(request):
    patients = Patient.objects.all()
    return render(request, "list.html", {'patients':patients})

def single_patient(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, "single.html", {'patient':patient})

def update_patient(request, id):
    context ={}
    patient = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST) 
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PatientForm()
    context["form"] = form
    return render(request, 'update.html', {'form':form, 'patient':patient})

@login_required(login_url='/login/')
def delete_patient(request, id):
    Patient.objects.filter(id=id).delete()
    return HttpResponseRedirect('/')