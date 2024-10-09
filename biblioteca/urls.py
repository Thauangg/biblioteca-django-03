from django.contrib import admin
from django.urls import path, include
from core.views import home  # Importe a view home

urlpatterns = [
    path('admin/', admin.site.urls),               # Rota para o admin
    path('api/', include('core.urls')),            # Inclua as URLs do app core
    path('', home, name='home'),  # Adicione esta linha para a página inicial
]
