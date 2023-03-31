import requests
from django.http import JsonResponse
from django.shortcuts import render

def get_wfs_data(request):
    # Define WFS URL
    wfs_url = 'https://ip-api.mobidata-bw.de/v1/NVBW/geoserver/ows?service=wfs&version=2.0.0&request=GetFeature&typeName=bikesharingStations&outputFormat=application/json'
    
    # Use requests library to retrieve data from WFS service
    response = requests.get(wfs_url)
    
    # Return JSON response
    return JsonResponse(response.json(), safe=False)


def map_page(request):
    # Call the get_wfs_data function to get the WFS data
    wfs_data = get_wfs_data(request)

    # Pass the data to the template
    return render(request, 'wfs_app/map.html', {'wfs_data': wfs_data})
