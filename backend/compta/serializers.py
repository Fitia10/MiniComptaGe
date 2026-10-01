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

    def validate_montant(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Le montant doit être supérieur à zéro."
            )

        return value

    def validate(self, data):

        if (
            data.get("compte_debit")
            and data.get("compte_credit")
            and data["compte_debit"] == data["compte_credit"]
        ):
            raise serializers.ValidationError(
                "Le compte débit et le compte crédit doivent être différents."
            )

        return data