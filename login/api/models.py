from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    phn = models.IntegerField(null=False)
    password = models.CharField(max_length=100)


class HealthHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 

