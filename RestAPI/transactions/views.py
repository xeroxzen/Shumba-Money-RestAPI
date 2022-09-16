from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from .permissions import IsOwnerOrReadOnly

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer