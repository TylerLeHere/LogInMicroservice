from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = length)) #Generate a random code that is k length
        if Room.objects.filter(code = code).count() == 0:
            break
    
    return code



# Create your models here.
#  Standard data base have columns, tables write python and interpret all of the data code for us
class Room(models.Model):
    username = models.CharField(max_length=8, default = "", unique = True)
    password = models.CharField(max_length=50, unique=True)
    remember_me = models.BooleanField(null = False, default = False)
    votes_to_skip = models.IntegerField(null = False, default = 1)
    created_at = models.DateTimeField(auto_now_add=True) 

