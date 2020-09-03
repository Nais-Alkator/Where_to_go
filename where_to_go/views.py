from django.shortcuts import render
from places.models import Place


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


