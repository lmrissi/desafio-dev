from django.db import models
from datetime import time

class CnabManager(models.Manager):
    def save_parsed_cnab(self, pased_cnab_dict_list):
        for dictionary in pased_cnab_dict_list:
            cnab = self.create(
                type=dictionary['type'],
                date=dictionary['date'],
                value=dictionary['value'],
                cpf=dictionary['cpf'],
                card=dictionary['card'],
                hour=dictionary['hour'],
                store_owner=dictionary['store_owner'],
                store_name=dictionary['store_name']
            )
        return cnab

class Cnab(models.Model):
    type = models.IntegerField()
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)

    objects = CnabManager()