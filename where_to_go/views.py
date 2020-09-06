from django.shortcuts import render
from places.models import Place, Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


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
                   "detailsUrl": "none",
                 }
        }
        features.append(place)

    data = {"data": {
              "type": "FeatureCollection",
              "features": features,
                        }
           }
    return render(request, "index.html", context=data)


def show_title(request, place_id):
    place = get_object_or_404(Place, place_id=place_id)
    data = {
            "title": place.title,
            "imgs": [image.image.url for image in place.place_image.all()],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude,               }
           }
    data = JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False, "indent": 2,})
    return data
