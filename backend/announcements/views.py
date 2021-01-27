from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

# from rest_framework import permissions
from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    # permission_classes = [permissions.IsAuthenticated]
