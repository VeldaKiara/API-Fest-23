from django.urls import path
from django.views.generic import TemplateView
from swags.views import SwagListView, SwagDetailView, SwagCreateView

app_name='swags'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('swags/', SwagListView.as_view(), name='swag-list'),
    path('swags/<uuid:pk>/', SwagDetailView.as_view(), name='swag-detail'),
    path('swags/create/', SwagCreateView.as_view(), name='swag-create'),
]