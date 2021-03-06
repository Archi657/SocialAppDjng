from django.db import models

from SocialApp.settings import TIME_ZONE
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #USER + user default my django + delete 
    image = models.ImageField(default='batman.png')
    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'


class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']
    def __str__(self) -> str:
        return f'{self.user.username} : {self.content}'