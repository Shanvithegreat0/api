from rest_framework import generics
from .models import Contact, SpamReport
from .serializers import ContactSerializer, SpamReportSerializer
from rest_framework.permissions import IsAuthenticated

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

class SpamReportCreateView(generics.CreateAPIView):
    queryset = SpamReport.objects.all()
    serializer_class = SpamReportSerializer
    permission_classes = [IsAuthenticated]
