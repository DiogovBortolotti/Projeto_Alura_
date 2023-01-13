from django.urls import path

from galeria.views import image, index

urlpatterns = [
    path('', index),
    path('imagem/',  image),
]
