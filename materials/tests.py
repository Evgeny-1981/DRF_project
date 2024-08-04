from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """Класс для проверки корректности работы CRUD уроков"""

    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru")
        self.course = Course.objects.create(name="Тестовый курс для проверки", )
        self.lesson = Lesson.objects.create(name="Тестовый урок для проверки",
                                            link_video="https://www.youtube.com/qwerty",
                                            owner=self.user, )
        self.client.force_authenticate(user=self.user)

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "name": "Тестовый урок для проверки",
            "link_video": "https://www.youtube.com/qwerty",
            "name_course": self.course.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_get", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)
        self.assertEqual(data.get("name_course"), self.lesson.name_course)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"name": "Тестовый урок обновлен"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.get(pk=self.lesson.pk).name, "Тестовый урок обновлен")

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


class SubscriptionTestCase(APITestCase):
    """Класс для проверки функционала работы подписки на обновления курса"""

    def setUp(self):
        self.user = User.objects.create(email="test@yandex.ru")
        self.course = Course.objects.create(name="Тестовая подписка на курс для проверки", )
        self.client.force_authenticate(user=self.user)
        self.url = reverse("materials:subscription_create")

    def test_subscription_create(self):
        data = {"user": self.user.pk, "course": self.course.pk}
        response = self.client.post(self.url, data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка добавлена")
        self.assertEqual(Subscription.objects.all().count(), 1)

    def test_subscribe_delete(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(self.url, data=data)
        temp_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(temp_data.get("message"), "Подписка удалена")
        self.assertEqual(Subscription.objects.all().count(), 0)
