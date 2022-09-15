from rest_framework import generics
from .models import Recipient
from .serializers import RecipientSerializer
from .permissions import IsOwnerOrReadOnly

class RecipientList(generics.ListCreateAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RecipientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

