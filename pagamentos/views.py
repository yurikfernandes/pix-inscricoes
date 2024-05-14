
from rest_framework import permissions, viewsets

from pagamentos.models import Pagamento
from pagamentos.serializers import PagamentoSerializer

# Create your views here.

class PagamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
