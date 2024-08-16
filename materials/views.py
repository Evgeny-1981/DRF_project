from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscription
from materials.paginators import CustomPagination
from materials.serilazers import (
    CourseSerializer,
    LessonSerializer,
    SubscriptionSerializer,
)
from users.permissions import IsModer, IsOwner
from materials.tasks import send_mail_about_course_updating


class CourseViewSet(viewsets.ModelViewSet):
    """Класс для просмотра, обновления, удаления курсов"""

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_permissions(self):
        """Метод проверяет права"""
        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (IsOwner,)
        return super().get_permissions()

    def perform_update(self, serializer):
        updated_course = serializer.save()
        send_mail_about_course_updating.delay(updated_course.id)
        updated_course.save()


class SubscriptionAPIView(APIView):
    """Класс для созданиия подписки пользователей"""

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = (
        IsAuthenticated,
        ~IsModer,
    )

    def post(self, *args, **kwargs):
        """Метод добавляет подписку на выбранный курс, если она отсутствует, иначе удаляет подписку"""
        user = self.request.user
        course_id = self.request.data.get("course")
        course_item = get_object_or_404(Course, pk=course_id)
        subscription_item = Subscription.objects.filter(user=user, course=course_item)

        if subscription_item.exists():
            subscription_item.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "Подписка добавлена"
        return Response({"message": message})


class LessonListAPIView(generics.ListAPIView):
    """Класс для просмотра уроков"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwner | IsModer,
    )
    pagination_class = CustomPagination


class LessonCreateAPIView(generics.CreateAPIView):
    """Класс для создания урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        ~IsModer,
    )


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Класс для обновления урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для просмотра информации по конкретному уроку"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления конкретного урока"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
