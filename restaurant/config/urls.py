from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from images.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
