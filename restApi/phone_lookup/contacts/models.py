from django.db import models
from users.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.phone_number}'

class SpamReport(models.Model):
    phone_number = models.CharField(max_length=15)
    reported_by = models.ForeignKey(User, related_name='spam_reports', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.phone_number} reported by {self.reported_by}'
