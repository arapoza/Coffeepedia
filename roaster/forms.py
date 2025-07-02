from django.forms import ModelForm
from django.urls import reverse
from .models import Roaster
from cities_light.models import Region, City

class RoasterForm(ModelForm):
    class Meta:
        model = Roaster
        fields = ["name", "country", "region", "city", "website"]

    def __init__(self, *args, **kwargs):
        country_id = kwargs.pop('country_id', None)
        region_id = kwargs.pop('region_id', None)

        super().__init__(*args, **kwargs)
        self.fields['region'].widget.attrs.update({
            "hx-get": reverse('roaster:city_dropdown'),
            "hx-trigger": "change",
            "hx-target": "#city-field",
            "hx-include": "closest form",
        })
        self.fields['region'].label_from_instance = lambda obj: obj.geoname_code
        self.fields['city'].label_from_instance = lambda obj: obj.name

        if country_id:
            self.fields['region'].queryset = Region.objects.filter(
                country_id=country_id)
        else:
            self.fields['region'].queryset = Region.objects.none()

        if region_id:
            self.fields['city'].queryset = City.objects.filter(
                region_id=region_id)
        else:
            self.fields['city'].queryset = City.objects.none()