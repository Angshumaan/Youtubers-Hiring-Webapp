from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import truncatechars
# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    # %y means year %y means month
    photo = models.ImageField(upload_to='media/slider/%Y/')
    links = models.CharField(max_length=255, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline


class About(models.Model):
    description = RichTextField()
    photo = models.ImageField(upload_to='media/slider/%Y/')

    def __str__(self):
        return self.description

    @property
    def short_description(self):
        return truncatechars(self.description, 100)
