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
                     "placeId": place.place_id,
                     "detailsUrl": reverse("details_url", args=[place.place_id]),
                 }
                 }
        features.append(place)

    data = {"data": {
        "type": "FeatureCollection",
        "features": features,
    }
    }
    return render(request, "index.html", context=data)


def get_place_info(request, place_id):
    place = get_object_or_404(Place, place_id=place_id)
    place_info = {
        "title": place.title,
        "imgs": [image.image.url for image in place.pictures.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude, }
    }
    place_info = JsonResponse(place_info, safe=False, json_dumps_params={
                               'ensure_ascii': False, "indent": 2, })
    return place_info
