# CONTACTS MODEL


from django.db import models

class User(models.Model):
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=40)
    email           = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Partner(models.Model):
    company         = models.CharField(max_length=60)

    def __unicode__(self):
        return self.company

class Agent(models.Model):
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=40)
    email           = models.EmailField()
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Relo_Company(models.Model):
    name            = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
