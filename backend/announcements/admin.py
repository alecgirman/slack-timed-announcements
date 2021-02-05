from django.contrib import admin

# Register your models here.

from announcements.models import Announcement


def enable_announcement(modeladmin, request, queryset):
    queryset.update(enabled=True)


enable_announcement.short_description = "Enable the selected announcements"


def disable_announcement(modeladmin, request, queryset):
    queryset.update(enabled=True)


disable_announcement.short_description = "Disable the selected announcements"


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["enabled", "title", "day", "time", "channel", "message"]
    actions = [enable_announcement, disable_announcement]


admin.site.register(Announcement, AnnouncementAdmin)
