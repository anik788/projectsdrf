import re
from django.shortcuts import render
import requests
import datetime

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else: 
        city = 'Dhaka'

    appid = 'dc56e9cf80a97e635a441b8c484dc993'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}

    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()
    return render(request, 'weatherapp/index.html', {'description': description,
    'icon': icon, 'temp': temp, 'day': day, 'city': city })




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.conf import settings
# import requests
# WEATHER_APP_ID = settings.WEATHER_APP_ID
# WEATHER_APP_ID = 'dc56e9cf80a97e635a441b8c484dc993'

# class WeatherAPIView(APIView):
#     @staticmethod
#     def get(request, *args, **kwargs):
#         try:
#             city_name = request.GET.get('city_name', 'London')
#             url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WEATHER_APP_ID}"
#             payload = ""
#             headers = {}
#             weather_app_response = requests.request("GET", url, headers=headers, data=payload).json()
#             result = {
#                 'id': weather_app_response['id'],
#                 'name': weather_app_response['name'],
#                 'weather': [{'id': we['id'], 'main': we['main'], 'description': we['description']} for we in weather_app_response['weather']],
#             }
#             return Response(result, status=status.HTTP_200_OK)
#         except Exception as ex:
#             print(str(ex))
#         return Response({"message": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)