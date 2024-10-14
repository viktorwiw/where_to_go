from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from places import views


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', views.index),
    path('places/<int:place_id>/', views.get_place)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
