from django.urls import path
from . import views

app_name = 'loginstuff'

urlpatterns = [
    path('', views.home, name='home'),
]
