from django.db import models


class CadastrialQuery(models.Model):
    objects = models.Manager()
    cadastrial_number = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    result = models.BooleanField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cadastrial_number} - {self.result}"
