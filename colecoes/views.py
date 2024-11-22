from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Colecao
from .serializers import ColecaoSerializer
from .permissions import IsColecionadorOrReadOnly

class ColecaoListCreate(ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsColecionadorOrReadOnly]

    def perform_create(self, serializer):
        # Associa a coleção ao usuário autenticado
        serializer.save(colecionador=self.request.user)

class ColecaoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsColecionadorOrReadOnly]
