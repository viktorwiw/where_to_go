from django.shortcuts import render
from django.conf import settings


def index(request):
    places_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.62, 55.793676]
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": settings.STATIC_URL + 'places/moscow_legends.json'
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [37.64, 55.753676]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": settings.STATIC_URL + 'places/roofs24.json'
                }
            }
        ]
    }
    context = {'places_geojson': places_geojson}
    return render(request, 'index.html', context)
