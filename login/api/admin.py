from django.contrib import admin
from .models import User, HealthHistory

# Register the room model.
admin.site.register([User, HealthHistory])