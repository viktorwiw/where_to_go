from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    extra = 1
    verbose_name_plural = "Фотографии"
    readonly_fields = ['get_preview']
    fields = ('image', 'get_preview', 'position')

    def get_preview(self, obj):
        return format_html('<img src="{}" width="{}" height="{}" />',
          obj.image.url,
            'auto',
            '200px'
            )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
