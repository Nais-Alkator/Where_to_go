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


def get_details_url(request, place_id):
    place = get_object_or_404(Place, place_id=place_id)
    details_url = {
            "title": place.title,
            "imgs": [image.image.url for image in place.place_image.all()],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude,               }
           }
    details_url = JsonResponse(details_url, safe=False, json_dumps_params={'ensure_ascii': False, "indent": 2,})
    return details_url