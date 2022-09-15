from rest_framework import generics, permissions
from .models import Recipient
from .serializers import RecipientSerializer

class RecipientList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer


class RecipientDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer