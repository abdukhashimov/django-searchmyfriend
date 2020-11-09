from django.db import models
from django.contrib.postgres.fields import ArrayField
from user.models import User

class Interest(models.Model):
    interests = ArrayField(models.CharField(max_length=500),size=100)
    user = models.ForeignKey(User, related_name='interests', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.interests}'

