from rest_framework import serializers
from .models import Contact, SpamReport

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'email']

class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ['id', 'phone_number', 'reported_by']
