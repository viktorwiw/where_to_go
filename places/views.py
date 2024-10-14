from django.shortcuts import render
from django.conf import settings

from places.models import Place


def index(request):
    places = Place.objects.all()

    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title_short,
                "placeId": place.id,
                "detailsUrl": settings.STATIC_URL + 'places/moscow_legends.json'
                }
            }
        places_geojson['features'].append(feature)

    context = {'places_geojson': places_geojson}
    return render(request, 'index.html', context)
