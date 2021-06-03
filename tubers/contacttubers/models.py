from django.db import models
from datetime import datetime
# Create your models here.


class Contacttuber(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255, blank=True)
    user_id = models.IntegerField(max_length=255, blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
