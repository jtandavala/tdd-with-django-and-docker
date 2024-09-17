from django.contrib import admin
from .models import Movie, CustomUser

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]

@admin.register(CustomUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ["username","email", "first_name","last_name"]
