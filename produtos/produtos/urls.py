from django.contrib import admin
from django.urls import path
from promotions.views import produto_list, produto_new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', produto_list, name='produto_list'),
    path('produtos/novo/', produto_new, name='produto_new'),
]
