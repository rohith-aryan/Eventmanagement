import requests
from geopy.geocoders import Nominatim

def fetch_weather(latitude, longitude, date):
    # Calculate city name using reverse geocoding
    geolocator = Nominatim(user_agent="event_finder")
    location = geolocator.reverse((latitude, longitude))
    city_name = location.raw['address'].get('city', None) if location else None
    
    # Call external Weather API to fetch weather data based on city name and date
    weather_api_url = f"https://gg-backend-assignment.azurewebsites.net/api/Weather?code=KfQnTWHJbg1giyB_Q9Ih3Xu3L9QOBDTuU5zwqVikZepCAzFut3rqsg==&city={city_name}&date={date}"
    response = requests.get(weather_api_url)
    weather_data = response.json()
    return weather_data

def calculate_distance(lat1, lon1, lat2, lon2):
    # Call external Distance Calculation API to calculate distance between two locations
    distance_api_url = f"https://gg-backend-assignment.azurewebsites.net/api/Distance?code=IAKvV2EvJa6Z6dEIUqqd7yGAu7IZ8gaH-a0QO6btjRc1AzFu8Y3IcQ==&latitude1={lat1}&longitude1={lon1}&latitude2={lat2}&longitude2={lon2}"
    response = requests.get(distance_api_url)
    distance_data = response.json()
    distance_km = distance_data['distance']
    return distance_km
