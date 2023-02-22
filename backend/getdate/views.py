import json
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. This is my first Django app.")
def gps_data(request):
    # Replace this with your code to get GPS data from the ESP32
    latitude = 35.681236
    longitude = 139.767125
    # Construct a dictionary to represent the GPS data
    gps_data = {'latitude': latitude, 'longitude': longitude}
    # Convert the dictionary to JSON format
    json_data = json.dumps(gps_data)
    # Return the GPS data as a JSON response
    return HttpResponse(json_data, content_type='application/json')
