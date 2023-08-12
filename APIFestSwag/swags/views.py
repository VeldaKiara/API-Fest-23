from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from swags.models import Swag
from swags.serializers import SwagSerializer

class SwagListView(ListAPIView):
    queryset = Swag.objects.all()
    serializer_class = SwagSerializer

class SwagDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Swag.objects.all()
    serializer_class = SwagSerializer

class SwagCreateView(generics.CreateAPIView):
    queryset = Swag.objects.all()
    serializer_class = SwagSerializer