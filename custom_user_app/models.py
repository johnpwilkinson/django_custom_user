from django.contrib.auth.models import AbstractUser
from django.db import models





# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length= 50, null=True)
    age = models.IntegerField(null=True)
    bio = models.TextField(blank=True, null=True)
    homepage = models.URLField(null=True)
    

    REQUIRED_FIELDS = ['age']

    def __str__(self):
        return self.username