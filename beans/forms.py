from django.forms import ModelForm
from .models import Bean
from users.models import Review

class BeanForm(ModelForm):
    class Meta:
        model = Bean
        fields = ["name", "roaster", "roast_level", "origin_type", "origin",
                   "process", "producer", "notes", "image"]


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["content", "rating"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = "Review Content"
        self.fields['rating'].label = "Rating (1-5)"
        self.fields['rating'].help_text = "Rate the beans from 1 (worst) to 5 (best)."