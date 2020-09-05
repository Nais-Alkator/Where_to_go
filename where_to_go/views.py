from django.shortcuts import render
from places.models import Place
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


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
    return HttpResponse(place.title)
