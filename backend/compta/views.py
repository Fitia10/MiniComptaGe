
from rest_framework import viewsets

from .models import Compte, Operation
from .serializers import CompteSerializer, OperationSerializer


class CompteViewSet(viewsets.ModelViewSet):
    queryset = Compte.objects.all()
    serializer_class = CompteSerializer


class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer