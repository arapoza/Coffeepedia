# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    # Optional: add extra fields here

    USERNAME_FIELD = 'email'              # Use email to log in
    REQUIRED_FIELDS = ['username']        # Still require handle during signup

    def __str__(self):
        return self.username  # or use self.get_full_name()
