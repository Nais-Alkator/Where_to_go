from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    
    def preview(self, image):
        if not image.image:
            return format_html('<p>Картинка ещё не загружена</p>', )

        return format_html('<img src="{}" height={} />', image.image.url, 200)
    

    readonly_fields = ["preview",]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ['place', 'position']
    raw_id_fields = ['place']

