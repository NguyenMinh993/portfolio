from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('health/', views.health_check, name='health_check'),
    path('photography/', views.photography, name='photography'),
    path('contact/', views.contact_form_submit, name='contact_form_submit'),
]
