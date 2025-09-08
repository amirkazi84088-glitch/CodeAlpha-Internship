from django.db import models

# Create your models here.
"""

class Bike(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='bike_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
# bike/models.py
from django.db import models
from django.contrib.auth.models import User"""

""""class Bike(models.Model):
    name        = models.CharField(max_length=100)
    brand       = models.CharField(max_length=100)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image       = models.ImageField(upload_to='bike/images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brand} {self.name}"
        """""

# bike/models.py
from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    """Extra fields for admin users."""
    user       = models.OneToOneField(User, on_delete=models.CASCADE)
    showroom_name = models.CharField(max_length=100, default='')
    phone      = models.CharField(max_length=15, default='')
    address    = models.CharField(max_length=200, default='')

    def __str__(self):
        return f"Admin: {self.user.username}"

class Bike(models.Model):
    """A bike available in the showroom."""
    name        = models.CharField(max_length=100)
    brand       = models.CharField(max_length=100)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image       = models.ImageField(upload_to='bikes/')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

class Booking(models.Model):
    """Store user bookings."""
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    bike      = models.ForeignKey(Bike, on_delete=models.CASCADE)
    date      = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.bike.name} on {self.date}"

class ContactMessage(models.Model):
    """Messages sent via Contact page."""
    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} at {self.sent_at}"


