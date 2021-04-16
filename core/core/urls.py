
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('loginstuff.urls', namespace="loginstuff")),
    path('patient/', include('patient.urls', namespace="patient")),
]
