from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def index(request):
    places = Place.objects.all()

    places_geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_info', args=[place.id]),
            }}
            for place in places
        ]
    }
    context = {'places_geojson': places_geojson}
    return render(request, 'index.html', context)


def get_place(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), pk=place_id)

    response = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }
    return JsonResponse(response, json_dumps_params={
        'ensure_ascii': False,
        'indent': 4
    })
