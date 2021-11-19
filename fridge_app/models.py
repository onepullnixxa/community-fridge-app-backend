from django.db import models

# Create your models here.
class Fridge(models.Model):
    fridge_name = models.CharField(max_length=100)
    image_url = models.TextField()
    needs_cleaning = models.BooleanField(default=False)
    canned_foods_needed = models.BooleanField(default=False)
    produce_needed = models.BooleanField(default=False)
    fruits_needed = models.BooleanField(default=False)
    maintenance_needed = models.BooleanField(default=False)

    def __str__(self):
        return self.fridge_name