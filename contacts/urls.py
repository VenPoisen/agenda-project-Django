from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>', views.open_contact, name='open_contact'),
]
