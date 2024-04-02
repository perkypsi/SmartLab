from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Enviroment, AccessLevel, Role, Profile, Project, Notification

class ProfileAdmin(UserAdmin):
    model = Profile
    list_display = ['patronymic', 'username']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Enviroment)
admin.site.register(AccessLevel)
admin.site.register(Role)
admin.site.register(Project)
admin.site.register(Notification)