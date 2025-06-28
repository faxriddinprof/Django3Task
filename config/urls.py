

from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add
    path('',home,name='home'),
    path('autos/', include('autos.urls')),                   # Add
    path('cats/', include('cats.urls')),

]
