from django.urls import path, include
from .views import create_event, EventViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'events/find', EventViewSet, basename='event')

urlpatterns = [
    path('event/', create_event, name='create_event'),
    path('', include(router.urls)),
]
