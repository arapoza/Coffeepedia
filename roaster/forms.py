from django.forms import ModelForm
from django.urls import reverse
from .models import Roaster
from cities_light.models import Region, City

class RoasterForm(ModelForm):
    class Meta:
        model = Roaster
        fields = ["name", "country", "region", "city", "website"]

    # Custom initialization to handle dynamic region and city dropdowns
    def __init__(self, *args, **kwargs):
        """Initialize the RoasterForm with dynamic region and city dropdowns."""
        country_id = kwargs.pop('country_id', None)
        region_id = kwargs.pop('region_id', None)

        super().__init__(*args, **kwargs)

        # Add HTMX attributes to the region field for dynamic loading of cities
        self.fields['region'].widget.attrs.update({
            "hx-get": reverse('roaster:city_dropdown'),
            "hx-trigger": "change",
            "hx-target": "#city-field",
            "hx-include": "closest form",
        })

        # Have the region field use the geoname_code for display
        self.fields['region'].label_from_instance = lambda obj: obj.geoname_code
        # Have the city field use the city name for display
        self.fields['city'].label_from_instance = lambda obj: obj.name

        # Set the initial queryset for the region dropdown based on the selected country
        if country_id:
            self.fields['region'].queryset = Region.objects.filter(
                country_id=country_id)
        else:
            self.fields['region'].queryset = Region.objects.none()

        # Set the initial queryset for the city dropdown based on the selected region
        if region_id:
            self.fields['city'].queryset = City.objects.filter(
                region_id=region_id)
        else:
            self.fields['city'].queryset = City.objects.none()