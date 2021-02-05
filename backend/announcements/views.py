from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

# from rest_framework import permissions
from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser


def announcement_list(request):
    announcement_objs = Announcement.objects.filter(enabled=True)
    serializer = AnnouncementSerializer(announcement_objs, many=True)
    return JsonResponse(serializer.data, safe=False)
