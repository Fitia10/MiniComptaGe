from rest_framework import viewsets

from .models import Compte, Operation
from .serializers import (
    CompteSerializer,
    OperationSerializer,
)


class CompteViewSet(viewsets.ModelViewSet):

    queryset = Compte.objects.all().order_by("code")
    serializer_class = CompteSerializer


class OperationViewSet(viewsets.ModelViewSet):

    queryset = Operation.objects.select_related(
        "compte_debit",
        "compte_credit"
    ).all().order_by("-date")

    serializer_class = OperationSerializer