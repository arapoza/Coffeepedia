from django.forms import ModelForm
from .models import Bean, Roaster

class BeanForm(ModelForm):
    class Meta:
        model = Bean
        fields = ["name", "roaster", "roast_level", "origin_type", "origin",
                   "process", "producer", "notes"]
        
class RoasterForm(ModelForm):
    class Meta:
        model = Roaster
        fields = ["name", "country", "region", "city", "website"]