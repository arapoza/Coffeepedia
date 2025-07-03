from django.db import models
from cities_light.models import City, Region, Country

# Create your models here.
class Roaster(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, name="country")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, name="region", blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, name="city", blank=True, null=True)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_number_of_beans(self):
        """Returns the number of beans associated with this roaster."""
        return self.beans.count()