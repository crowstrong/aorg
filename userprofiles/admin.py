from django.contrib import admin

from userprofiles.models import Documents, UserProfile

admin.site.register(UserProfile)
admin.site.register(Documents)
