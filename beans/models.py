from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cities_light.models import City, Region, Country


# Create your models here.
class Roaster(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, name="country", default="United States")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, name="region", blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, name="city", blank=True, null=True)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"


class Bean(models.Model):
    LIGHT = "L"
    LIGHT_MEDIUM = "LM"
    MEDIUM = "M"
    MEDIUM_DARK = "MD"
    DARK = "D"
    ROAST_LEVEL_CHOICES = {
        (LIGHT, "Light"),
        (LIGHT_MEDIUM, "Light-Medium"),
        (MEDIUM, "Medium"),
        (MEDIUM_DARK, "Medium-Dark"),
        (DARK, "Dark"),
    }

    WASHED = "W"
    NATURAL = "N"
    HONEY = "H"
    CROSS_FERMENTED = "CF"
    PROCESS_CHOICES = {
        (WASHED, "Washed"),
        (NATURAL, "Natural"),
        (HONEY, "Honey"),
        (CROSS_FERMENTED, "Cross fermented"),
    }

    BLEND = "B"
    SINGLE_ORIGIN = "SO"
    ORIGIN_TYPE_CHOICES = {
        (BLEND, "Blend"),
        (SINGLE_ORIGIN, "Single origin"),
    }

    name = models.CharField(max_length=100)
    roaster = models.ForeignKey(Roaster, on_delete=models.CASCADE)
    roast_level = models.CharField(
        max_length=2,
        choices=ROAST_LEVEL_CHOICES,
        default=MEDIUM,
    )
    origin_type = models.CharField(
        max_length=2,
        choices=ORIGIN_TYPE_CHOICES,
        default=BLEND,
    )
    origin = models.CharField(max_length=50)
    process = models.CharField(
        max_length=2,
        choices=PROCESS_CHOICES,
        default=WASHED,
    )
    producer = models.CharField(max_length=50)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return f"Name: {self.name}\n \
                 roastery: {self.roaster}\n \
                 roast level: {self.roast_level}\n \
                 origin: {self.origin}\n \
                 process: {self.process}\n \
                 producer: {self.producer}\n \
                 notes: {self.notes}"