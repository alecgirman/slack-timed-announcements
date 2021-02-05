from django.contrib import admin

# Register your models here.

from announcements.models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["enabled", "title", "day", "time", "channel", "message"]


admin.site.register(Announcement, AnnouncementAdmin)
