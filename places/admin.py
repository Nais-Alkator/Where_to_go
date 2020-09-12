from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin


admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    
    def preview(self, image):
        return format_html('<img src="{}" height={} />'.format(image.image.url, 200)
    )

    readonly_fields = ["preview",]
    fields = ('image', "preview", "position")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


