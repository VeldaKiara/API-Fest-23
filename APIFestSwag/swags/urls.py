from django.urls import path
from django.views.generic import TemplateView
from swags.views import SwagListView, SwagDetailView

app_name='swags'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('swag/', SwagListView.as_view(), name='swag-list'),
    path('swag/<uuid:pk>/', SwagDetailView.as_view(), name='swag-detail'),
]