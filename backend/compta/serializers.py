from rest_framework import serializers
from .models import Compte, Operation


class CompteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compte
        fields = "__all__"


class OperationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = "__all__"