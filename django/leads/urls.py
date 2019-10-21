from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls
