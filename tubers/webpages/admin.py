from django.contrib import admin
from .models import Slider, Team, About
from django.utils.html import format_html

# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        # displaying photo by fromatting and passing it in list_display
        return format_html('<img src ="{}" width="40"/>'.format(object.photo.url))

    # displayin every field n admin panel
    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    list_display_links = ('id', 'first_name')  # displaying clickable link
    # it will unlock search field based on fields.
    search_fields = ('first_name', 'role')
    # Filter by role That we see in right hand side as capitalize FILTER
    list_filter = ('role',)


class TeamSlider(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src ="{}" width="40"/>'.format(object.photo.url))
    list_display = ('id', 'myphoto', 'headline', 'button_text')
    list_display_links = ('id', 'headline')

    search_fields = ('id',)
    list_filter = ('id',)


class AboutUs(admin.ModelAdmin):
    list_display = ('id', 'short_description')


admin.site.register(Slider, TeamSlider)
admin.site.register(Team, TeamAdmin)
admin.site.register(About, AboutUs)
