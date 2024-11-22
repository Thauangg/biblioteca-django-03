from django.contrib import admin
from django.urls import path, include
from core.views import home  # Importe a view home do app core
from colecoes.views import ColecaoListCreate, ColecaoDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o admin
    path('', home, name='home'),  # Rota para a página inicial (Home)
    
    # Rotas do app 'colecoes' (API)
    path('colecoes/', ColecaoListCreate.as_view(), name='colecao-list'),  # Listagem e criação de coleções
    path('colecoes/<int:pk>/', ColecaoDetail.as_view(), name='colecao-detail'),  # Visualizar, editar e excluir coleções
    
    # Rotas de autenticação com JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Documentação da API usando drf-spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Rotas do app 'core' (API)
    path('api/', include('core.urls')),  
]
