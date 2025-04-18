from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class User(AbstractUser):
    MEMBERSHIP_ADMIN = 'A'
    MEMBERSHIP_USER = 'U'
    MEMBERSHIP_MODERATOR = 'M'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_ADMIN, 'ADMIN'),
        (MEMBERSHIP_USER, 'USER'),
        (MEMBERSHIP_MODERATOR, 'MODERATOR'),
    ]

    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_USER)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def type_to_string(self):
        if self.role == "A":
            return "Admin"
        elif self.role == "U":
            return "User"
        elif self.role == "M":
            return "Moderator"


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='avatar')
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='store/images', blank=True)


    def __str__(self):
        return f"Photo by {self.user.username}"
    
    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name