from django.contrib import admin

# Register your models here.

from announcements.models import Announcement


def enable_announcement(modeladmin, request, queryset):
    queryset.update(enabled=True)


enable_announcement.short_description = "Enable the selected announcements"


def disable_announcement(modeladmin, request, queryset):
    queryset.update(enabled=True)


disable_announcement.short_description = "Disable the selected announcements"


def move_to_general(modeladmin, request, queryset):
    queryset.update(channel="general")


move_to_general.short_description = "Move the selected announcements to #general"


def move_to_botlogging(modeladmin, request, queryset):
    queryset.update(channel="bot-logging")


move_to_botlogging.short_description = "Move the selected announcements to #bot-logging"


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["title", "enabled", "day", "time", "channel", "message"]
    actions = [
        enable_announcement,
        disable_announcement,
        move_to_general,
        move_to_botlogging,
    ]


admin.site.register(Announcement, AnnouncementAdmin)
