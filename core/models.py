from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categorie = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nom


class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)  # <-- ajout
    quantite = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # mise à jour du stock automatiquement
        self.total = self.produit.prix * self.quantite
        self.produit.stock -= self.quantite
        self.produit.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produit.nom} x {self.quantite} ({self.client.nom if self.client else 'Sans client'})"


class Dette(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payee = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.nom} - {self.montant} CFA"
