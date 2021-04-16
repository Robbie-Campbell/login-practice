from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import PatientForm
from .models import Patient, D2A

def patient_search(request):
    model = Patient
    context_object_name = 'all_search_results'
    results = []
    query = request.GET.get('search')
    if query:
        postresult = Patient.objects.filter(first_name__contains=query)
        results = postresult
    else:
        results = None
    return render(request, "search.html", {'results':results})

def insert_patient(request):
    form = PatientForm
    if request.method == 'POST':
        form = PatientForm(request.POST) 
        if form.is_valid(): 
            task = form.save()
            return HttpResponseRedirect("/")
    else:
        form = PatientForm()
    return render(request, 'patient/insert.html', {'form':form})

def list_patients(request):
    patients = Patient.objects.all()
    return render(request, "patient/list.html", {'patients':patients})

def single_patient(request, id):
    patient = Patient.objects.get(id=id)
    d2as = D2A.objects.filter(patient_id=id)
    return render(request, "patient/single.html", {'patient':patient, 'd2as':d2as})

def d2a_single(request, id):
    d2a = D2A.objects.get(id=id)
    return render(request, "d2a/single.html", {'d2a':d2a})

# def update_patient(request, id):
#     context ={}
#     patient = get_object_or_404(Patient, id=id)
#     form = PatientForm(request.POST or None, instance=patient)
#     if request.method == 'POST':
#         form = PatientForm(request.POST) 
#         if form.is_valid(): 
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = PatientForm()
#     context["form"] = form
#     return render(request, 'update.html', {'form':form, 'patient':patient})

@login_required(login_url='/login/')
def delete_patient(request, id):
    Patient.objects.filter(id=id).delete()
    return HttpResponseRedirect('/')