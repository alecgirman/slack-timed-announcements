from announcements.models import Announcement
from rest_framework import serializers


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ["day", "time", "channel", "message"]
