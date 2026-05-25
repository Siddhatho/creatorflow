from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('creator', 'Creator'),
        ('reviewer', 'Reviewer'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='creator')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

    def is_admin(self):
        return self.role == 'admin'

    def is_creator(self):
        return self.role == 'creator'

    def is_reviewer(self):
        return self.role == 'reviewer'