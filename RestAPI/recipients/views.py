from rest_framework import viewsets
from .models import Recipient
from .serializers import RecipientSerializer
from .permissions import IsOwnerOrReadOnly

class RecipientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

