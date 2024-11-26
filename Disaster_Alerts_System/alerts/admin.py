# alerts/admin.py
from django.contrib import admin
from .models import DisasterAlert  # Vérifie l'importation du bon modèle

admin.site.register(DisasterAlert)
