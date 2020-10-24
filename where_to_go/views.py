from django.shortcuts import render
from places.models import Place, Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        place = {"type": "Feature",
                 "geometry": {
                     "type": "Point",
                     "coordinates": [place.longitude, place.latitude]
                 },
                 "properties": {
                     "title": place.title,
                     "placeId": place.slug,
                     "detailsUrl": reverse("place_info", args=[place.slug]),
                 }
                 }
        features.append(place)

    place_info = {"place_info": {
        "type": "FeatureCollection",
        "features": features,
    }
    }
    return render(request, "index.html", context=place_info)


def get_place_info(request, slug):
    place = get_object_or_404(Place, slug=slug)
    serialized_place = {
        "title": place.title,
        "imgs": [image.image.url for image in place.pictures.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude, }
    }
    return JsonResponse(serialized_place, safe=False, json_dumps_params={
                               'ensure_ascii': False, "indent": 2, })
    
