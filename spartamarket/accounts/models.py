from django.db import models
from django.contrib.auth.models import AbstractUser


def user_profile_image_path(instance, filename):
    return f'profile_images/{instance.username}/{filename}'

class User(AbstractUser):
    # 프로필 이미지
    profile_image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)
    
    
    # 팔로우
    follows = models.ManyToManyField('self', symmetrical=False, related_name="followers", blank=True)
    
    
    # 팔로우 수
    @property
    def follower_count(self):
        return self.followers.count()
    
    @property
    def following_count(self):
        return self.follows.count()
    
    def __str__(self):
        return self.username