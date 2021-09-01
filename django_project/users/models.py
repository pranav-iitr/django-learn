from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE)
    image=models.ImageField(default="default.jpeg", upload_to="profile_pics", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f'{self.user.username} Profile'