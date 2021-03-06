from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:chapterpath>/<slug:path>/", views.file_view, name="fileview"),
    path("latestpage/", views.latestpage, name="latestpage")
]