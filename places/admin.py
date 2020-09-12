from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html

admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    
    def preview(self, image):
        return format_html('<img src="{}" height={} />'.format(image.image.url, 200)
    )

    readonly_fields = ["preview",]
    fields = ('image', 'place_image', "image_id", "preview")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


