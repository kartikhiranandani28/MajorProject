from django.db import models
from django.contrib.auth.models import User

class College(models.Model):
    COLLEGE_TYPE_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]

    college_name = models.CharField(max_length=255)
    college_type = models.CharField(max_length=10, choices=COLLEGE_TYPE_CHOICES)
    contact_no = models.CharField(max_length=15)
    course = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model

    def __str__(self):
        return self.college_name
