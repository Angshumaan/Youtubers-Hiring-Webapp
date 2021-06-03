from django.contrib import admin
from .models import Hiretuber
# Register your models here.


class TeamHiretuber(admin.ModelAdmin):
    # displayin every field n admin panel
    list_display = ('id', 'first_name', 'last_name', 'email', 'tuber_name')
    list_display_links = ('id', 'first_name')  # displaying clickable link
    # it will unlock search field based on fields.
    search_fields = ('first_name',)


admin.site.register(Hiretuber, TeamHiretuber)
