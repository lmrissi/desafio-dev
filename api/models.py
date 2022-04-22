from tkinter import CASCADE
from django.db import models
from datetime import time

class CnabTransactions(models.Model):
    type = models.IntegerField(unique=True)
    description = models.CharField(max_length=30)
    nature = models.CharField(max_length=10)
    signal = models.CharField(max_length=1)

class Store(models.Model):
    owner = models.CharField(max_length=14)
    name = models.CharField(max_length=19)

    def calculate_total(self):
        cnabs = Cnab.objects.filter(store=self)
        return sum(cnab.get_values() for cnab in cnabs)

class Cnab(models.Model):
    type = models.ForeignKey(CnabTransactions, to_field="type", on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)

    def get_values(self):
        if self.type.nature == 'Entrada':
            return self.value
        else:
            return self.value*(-1)