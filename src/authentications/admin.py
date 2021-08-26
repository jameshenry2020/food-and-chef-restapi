from django.contrib import admin
from django.db.models.deletion import ProtectedError
from .models import User, Profile, ChefBook
# Register your models here.

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(ChefBook)