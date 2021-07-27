from django.db import models
from accounts.models import CustomUser

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    telephone = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Show(models.Model):
    artists = models.ForeignKey(to=CustomUser, related_name='show_artist', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media')
    venue = models.ForeignKey(to=Venue, related_name='venue_show', on_delete=models.SET_NULL, blank=True, null=True)
    show_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


