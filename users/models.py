from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intructor = models.CharField(max_length=300)
    image = models.ImageField(default='default.jpg', upload_to='images')
    def __str__(self):
        return f'{self.user} Profile'
    

@receiver(post_save, sender=User)
def creat_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
            instance.profile.save()