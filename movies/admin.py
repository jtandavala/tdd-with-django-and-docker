from django.contrib import admin
from .models import Movie, CustomUser

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ["title","genre","year", "updated_date"]
    list_display = ["title", "genre", "year", "created_date", "updated_date"]
    readonly_fields = ["created_date", "updated_date"]

@admin.register(CustomUser)
class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ["username","email", "first_name","last_name"]
