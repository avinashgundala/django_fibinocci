from django.db import models

class Fibinocci(models.Model):
    element = models.BigIntegerField()
    value = models.TextField()
    time_taken = models.CharField(max_length=16)

    class Meta:
        ordering = ['element']

    def __str__(self):
        return str(self.element)
