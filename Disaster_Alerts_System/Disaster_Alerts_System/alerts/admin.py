from django.contrib import admin
from .models import Alert, DisasterAlert, UserProfile

admin.site.register(Alert)
admin.site.register(DisasterAlert)
admin.site.register(UserProfile)
