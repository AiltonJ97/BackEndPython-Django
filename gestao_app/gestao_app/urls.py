from django.contrib import admin
from django.urls import path
from promotions.views import helloworld
from promotions.views import lista_alunos, lista_cursos

urlpatterns = [
    path('hello', helloworld),
    path("admin/promotions/alunos/", lista_alunos, name="Alunos"),
    path("cursos/", lista_cursos, name="Cursos"),

    path('admin/', admin.site.urls),
]
