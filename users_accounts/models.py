from django.db import models
from django.contrib.auth.models import User
from PIL import Image as Im

# Create your models here.
class Customer(models.Model):
    CHOICES = (
        ('Employer', 'Employer'),
        ('user', 'user'),
    )
    category = models.CharField(max_length=20, choices=CHOICES, default='user')

    def __str__(self):
        return self.category

from django.db import models

class TermsOfService(models.Model):
    contents = models.TextField()
    date_updated = models.DateTimeField(auto_now=True)
    
class Earnings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields

class PendingPayments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields

class WithdrawalRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    is_approved = models.BooleanField(default=False)
    # Other fields


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    profile_pictures = models.ImageField(unique=True, default='img.png', upload_to='pics')
    work_bio = models.TextField(default='write a short bio about yourself')
    mobile_number = models.IntegerField(default="123...")
    dob = models.DateField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default="Gender")
    category = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField(default="search content")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    STATUS_CHOICES = [
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
    ]
    client = models.CharField(max_length=100)
    deadline = models.DateField(default="Deadline")
    title = models.CharField(max_length=255, default="Job Title")
    status = models.CharField(max_length=200, choices=STATUS_CHOICES ,default="In Progress")

    def __str__(self):
        return self.first_name
        return self.title

    def save(self):
        super().save()
        img = Im.open(self.profile_pictures.path)

        if img.height > 90 or img.width > 90:
            output_size = (90, 90)
            img. thumbnail(output_size)
            img.save(self.profile_pictures.path)
