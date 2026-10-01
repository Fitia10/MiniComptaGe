from django.contrib import admin
from .models import Compte, Operation


@admin.register(Compte)
class CompteAdmin(admin.ModelAdmin):
    list_display = ("code", "libelle", "type")
    search_fields = ("code", "libelle")
    list_filter = ("type",)


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "libelle",
        "compte_debit",
        "compte_credit",
        "montant",
    )

    search_fields = ("libelle",)
    list_filter = ("date",)