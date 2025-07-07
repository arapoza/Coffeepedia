from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Review


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['username'].help_text = "This will be your public display name."


class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # Assuming the Review model is linked to User
        fields = ['content', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = "Review Content"
        self.fields['rating'].label = "Rating (1-5)"
        self.fields['rating'].help_text = "Rate the beans from 1 (worst) to 5 (best)."