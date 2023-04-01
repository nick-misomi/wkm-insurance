from django.db import models

# Create your models here.

class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
