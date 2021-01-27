from django.contrib import admin

# Register your models here.

from announcements.models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["day", "time", "channel", "message"]


admin.site.register(Announcement, AnnouncementAdmin)
