from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django_tests import settings
from portfolio.views import home, projets_index, projets_details

urlpatterns = [
    path('', home, name='home'),
    path('projets/', projets_index, name='projets'),
    path('projets/<str:slug>/', projets_details, name='projet'),
    path('admin/', admin.site.urls),
]

if not settings.IN_DOCKER:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
