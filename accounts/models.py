from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    UNIQUE_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + '-' + self.last_name

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + '-' + self.last_name)
        return super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(to=CustomUser, related_name="artist", primary_key=True, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    web_link = models.URLField(max_length=255, blank=True, null=True)
    zip_code = models.SmallIntegerField(null=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    brand_logo = models.ImageField(upload_to='images')
    company_documents = models.FileField(upload_to='images')
    facebook_link = models.URLField(max_length=255, blank=True, null=True)
    instagram_link = models.URLField(max_length=255, blank=True, null=True)
    twitter_link = models.URLField(max_length=255, blank=True, null=True)
    LinkedIn_link = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.artist.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.artist.save()
