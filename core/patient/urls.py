from django.urls import path
from . import views

app_name = "patient"

urlpatterns = [
    path('insert/', views.insert_patient),
    path('list/', views.list_patients),
    path('single/<int:id>', views.single_patient),
    path('update/<int:id>', views.update_patient),
    path('delete/<int:id>', views.delete_patient),
]