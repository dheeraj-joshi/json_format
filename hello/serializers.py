from rest_framework import serializers
from .models import LogMessage

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=LogMessage
        fields=['message','log_date']