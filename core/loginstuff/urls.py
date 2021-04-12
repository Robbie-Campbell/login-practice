from django.urls import path
from . import views

app_name = 'loginstuff'

urlpatterns = [
    path('', views.home),
    path('insert/', views.insert_name)
]
