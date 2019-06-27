from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from images.views import index, main_banner

urlpatterns = [
    path('', index, name='index'),
    path('main/<int:pk>/', main_banner, name='main-banner'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
