from django.urls import path

from galeria.views import image, index

urlpatterns = [
    path('', index, name='index'),
    path('imagem/',  image, name='imagem'),
]
