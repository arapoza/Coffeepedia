# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

from beans.models import Bean  # Assuming Bean model is defined in roaster app

class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    # Optional: add extra fields here

    USERNAME_FIELD = 'email'              # Use email to log in
    REQUIRED_FIELDS = ['username']        # Still require handle during signup

    def __str__(self):
        return self.username  # or use self.get_full_name()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    bean = models.ForeignKey(Bean, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Assuming rating is an integer, e.g., 1-5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
    
    class Meta:
        ordering = ['-created_at']  # Newest reviews first