from django.db import models
from datetime import time

class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents', max_length=100, blank=True)

class CnabManager(models.Manager):
    def save_parsed_cnab(self, pased_cnab_dict_list):
        for dict in pased_cnab_dict_list:
            cnab = self.create(
                type=dict['type'],
                date=dict['date'],
                value=dict['value']/100,
                cpf=dict['cpf'],
                card=dict['card'],
                hour=time(
                    dict['hour'][0:2],
                    dict['hour'][2:4],
                    dict['hour'][4:6],
                ),
                store_owner=dict['store_owner'],
                store_name=dict['store_name']
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