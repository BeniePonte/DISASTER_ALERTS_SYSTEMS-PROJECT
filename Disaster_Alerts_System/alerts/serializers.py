from rest_framework import serializers
from .models import DisasterAlert

class DisasterAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterAlert
        fields = ['type', 'location', 'severity', 'description', 'timestamp']
        extra_kwargs = {
            'type': {'required': True},  # Assurez-vous que ce champ est obligatoire
            'location': {'required': True},
            'severity': {'required': True},
        }
