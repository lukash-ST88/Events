from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    registration_data = models.DateTimeField(auto_now_add=True)
    birthdate = models.DateField(null=True)


class Event(models.Model):
    title = models.CharField(max_length=255, null=False)
    text = models.TextField(null=False)
    creation_date = models.DateField(null=False)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name='event_creator')
    participants = models.ManyToManyField(CustomUser, null=False, related_name='event_participant')


