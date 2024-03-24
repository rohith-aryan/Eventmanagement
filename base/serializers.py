from rest_framework import serializers
from .models import Event
from .helpers import fetch_weather, calculate_distance

class EventSerializer2(serializers.ModelSerializer):
    weather = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['event_name', 'city_name', 'date', 'weather', 'distance']

    def get_weather(self, obj):
        latitude = self.context["request"].query_params.get('latitude')
        longitude = self.context["request"].query_params.get('longitude')
        date = obj.date
        weather_data = fetch_weather(latitude, longitude, date)
        return weather_data

    def get_distance(self, obj):
        latitude1 = self.context["request"].query_params.get('latitude')
        longitude1 = self.context["request"].query_params.get('longitude')
        latitude2 = obj.latitude
        longitude2 = obj.longitude
        if latitude1 and longitude1:
            distance = calculate_distance(latitude1, longitude1, latitude2, longitude2)
            return distance
        return None
