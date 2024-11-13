from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()

    places_geojson = {
        'type': 'FeatureCollection',
        'features': []
    }

    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_info', args=[place.id]),
                }
            }
        places_geojson['features'].append(feature)

    context = {'places_geojson': places_geojson}
    return render(request, 'index.html', context)


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = place.images.all()

    response = {
        'title': place.title,
        'imgs': [],
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }
    for image in images:
        response['imgs'].append(image.image.url)
    return JsonResponse(response, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4
    })
