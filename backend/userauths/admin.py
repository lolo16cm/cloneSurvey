from django.contrib import admin
from userauths.models import User, Profile
# Register your models here.

#list_display is a built-in attribute provided by Django's ModelAdmin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'date']

admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)