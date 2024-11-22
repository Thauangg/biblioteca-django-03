from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsColecionadorOrReadOnly(BasePermission):
    """
    Permite edição apenas para o colecionador. Outros usuários podem visualizar.
    """

    def has_object_permission(self, request, view, obj):
        # Métodos de leitura (GET, HEAD, OPTIONS) são permitidos para todos
        if request.method in SAFE_METHODS:
            return True

        # Permissão de escrita apenas para o colecionador
        return obj.colecionador == request.user
