from django.urls import path
from announcements import views

urlpatterns = [
    path("announcements/", views.announcement_list),
]
