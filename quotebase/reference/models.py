# REFERENCE MODEL

from django.db import models


class Airline(models.Model):
    code            = models.CharField(max_length=3)
    name            = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Currency(models.Model):
    code            = models.CharField(max_length=3)
    name            = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Referral_Fee(models.Model):
    relo_company    = models.ForeignKey('contacts.Relo_Company')
    fee             = models.IntegerField()
    notes           = models.TextField()
