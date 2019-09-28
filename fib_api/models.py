from django.db import models

class Fibinocci(models.Model):
    element = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        ordering = ['element']

    def __str__(self):
        return str(self.element)
