from rest_framework import status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer2
from .helpers import fetch_weather, calculate_distance
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim

@api_view(['POST'])
def create_event(request):
    if request.method == 'POST':
        serializer = EventSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer2
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Handle query params for filtering, such as city_name, date__gte, etc.
        city_name = self.request.query_params.get('city_name')
        if city_name:
            queryset = queryset.filter(city_name=city_name)

        # Filter events occurring within the next 14 days from the specified date
        search_date = self.request.query_params.get('date')
        if search_date:
            search_datetime = datetime.strptime(search_date, "%Y-%m-%d")
            end_date = search_datetime + timedelta(days=14)
            queryset = queryset.filter(date__range=[search_datetime, end_date])

        # Handle limit and offset for pagination
        limit = self.request.query_params.get('limit')
        if limit:
            queryset = queryset[:int(limit)]
        
        offset = self.request.query_params.get('offset')
        if offset:
            queryset = queryset[int(offset):]

        return queryset
