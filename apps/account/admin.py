from django.contrib import admin
from .models import NewUser

# register the user model on the admin page
admin.site.register(NewUser)