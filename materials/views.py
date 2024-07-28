from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from materials.models import Course, Lesson
from materials.serilazers import CourseSerializer, LessonSerializer
from users.permissions import IsModer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (AllowAny,)

    # def get_permissions(self):
    #     if self.action == 'create':
    #         self.permission_classes = [IsOwner]
    #     elif self.action == 'list':
    #         self.permission_classes = [список пермишенов для этого эндпоинта]
    #     return [permission() for permission in permission_classes]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def get_permissions(self):


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
