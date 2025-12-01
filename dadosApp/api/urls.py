from django.urls import path
from .views import Usuarios

urlpatterns = [
    path('usuarios/', Usuarios.as_view()),
]

