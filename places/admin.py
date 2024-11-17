from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    extra = 1
    verbose_name_plural = 'Фотографии'
    readonly_fields = ['get_preview']
    fields = ('image', 'get_preview', 'position')

    def get_preview(self, obj):
        return format_html(
            '<img src={} style="max-width:{}; max-height:{};" />',
            obj.image.url,
            '200px',
            '200px'
            )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(SortableAdminBase, admin.ModelAdmin):
    autocomplete_fields = ['place']
    fields = ('image', 'get_preview_image')
    readonly_fields = ['get_preview_image']

    def get_preview_image(self, obj):
        return format_html(
            '<img src={} style="max-width:{}; max-height:{};" />',
            obj.image.url,
            '200px',
            '200px'
            )