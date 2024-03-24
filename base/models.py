from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

    def __str__(self):
        return f"{self.event_name} in {self.city_name} on {self.date} at {self.time}"
