from django.contrib import admin
from .models import Place, Image


admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    fields = ('image', 'place_image', "image_id")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

