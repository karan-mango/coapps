from django.urls import path
from .views import add_lead, lead_list,edit_lead

urlpatterns = [
    path('add/', add_lead, name='add'),
    path('list/', lead_list, name='lead_list'),
    path('edit/<int:lead_id>/', edit_lead, name='edit_lead'),
]
