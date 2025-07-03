from django.forms import ModelForm
from .models import Bean

class BeanForm(ModelForm):
    class Meta:
        model = Bean
        fields = ["name", "roaster", "roast_level", "origin_type", "origin",
                   "process", "producer", "notes", "image"]