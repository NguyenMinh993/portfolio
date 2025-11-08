from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photography/', views.photography, name='photography'),
    path('contact/', views.contact_form_submit, name='contact_form_submit'),
]
