from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

# from rest_framework import permissions
from announcements.models import Announcement
from announcements.serializers import AnnouncementSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# class AnnouncementViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """

#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     def create(self, request, **kwargs):
#         print(request)
#         return Announcement.objects.create(**kwargs)


def announcement_list(request):
    announcement_objs = Announcement.objects.all()
    serializer = AnnouncementSerializer(announcement_objs, many=True)
    return JsonResponse(serializer.data, safe=False)
