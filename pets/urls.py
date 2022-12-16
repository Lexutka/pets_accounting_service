from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('api/pets/<str:pet_id>/photo', views.PhotoView.as_view()),
    path('api/pets', views.PetView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
