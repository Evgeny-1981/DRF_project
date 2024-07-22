from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
    LessonDestroyAPIView,
)

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path(
        "lessons/update/<slug:slug>/",
        LessonUpdateAPIView.as_view(),
        name="lesson_update",
    ),
    path("lessons/<slug:slug>/", LessonRetrieveAPIView.as_view(), name="lesson_get"),
    path(
        "lessons/delete/<slug:slug>",
        LessonDestroyAPIView.as_view(),
        name="lesson_delete",
    ),
] + router.urls
