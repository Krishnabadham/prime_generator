from django.urls import path
from . import views
urlpatterns =[path('',views.generate_primes,name='primes')]