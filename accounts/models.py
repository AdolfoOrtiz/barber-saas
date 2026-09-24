from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Campo adicional para diferenciar roles
    ROLE_CHOICES = (
        ('superadmin', 'Superadministrador'),
        ('owner', 'Dueño de Barbería'),
        ('barber', 'Barbero'),
        ('client', 'Cliente'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    # Campos opcionales adicionales
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
