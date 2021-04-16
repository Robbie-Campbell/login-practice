from django.urls import path
from . import views

app_name = "patient"

urlpatterns = [
    path('insert/', views.insert_patient, name="insert"),
    path('list/', views.list_patients, name="list"),
    path('single/<int:id>', views.single_patient, name="single"),
    # path('update/<int:id>', views.update_patient),
    path('delete/<int:id>', views.delete_patient),
    path('search/', views.patient_search, name='search'),
    path('d2a/<int:id>', views.d2a_single, name='d2a'),
]