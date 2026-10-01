from django.db import models


class Compte(models.Model):

    TYPE_CHOICES = [
        ("ACTIF", "Actif"),
        ("PASSIF", "Passif"),
        ("CHARGE", "Charge"),
        ("PRODUIT", "Produit"),
    ]

    code = models.CharField(
        max_length=20,
        unique=True
    )

    libelle = models.CharField(
        max_length=150
    )

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    def __str__(self):
        return f"{self.code} - {self.libelle}"


class Operation(models.Model):

    date = models.DateField()

    libelle = models.CharField(
        max_length=255
    )

    compte_debit = models.ForeignKey(
        Compte,
        on_delete=models.PROTECT,
        related_name="operations_debit"
    )

    compte_credit = models.ForeignKey(
        Compte,
        on_delete=models.PROTECT,
        related_name="operations_credit"
    )

    montant = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.libelle