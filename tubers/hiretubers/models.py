from django.db import models
from datetime import datetime
# Create your models here.


class Hiretuber(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    tuber_id = models.IntegerField(max_length=255, blank=True)
    tuber_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    message = models.TextField(max_length=255, blank=True)
    user_id = models.IntegerField(max_length=255, blank=True)
    phone = models.CharField(max_length=255)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
