from django.contrib import admin
from userauths.models import Profile, User

class UserAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "username"]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["full_name", "address", "user", "pid", "date"]
    search_fields = ["full_name"]

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)