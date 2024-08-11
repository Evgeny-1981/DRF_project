from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.serviсes import convert_usd_to_rub
from materials.validators import validate_allowed_links


class LessonSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    link_video = serializers.URLField(validators=[validate_allowed_links])
    price_rub = serializers.SerializerMethodField()

    def get_price_rub(self, lesson):
        return convert_usd_to_rub(lesson.price_usd)

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(source="lesson", many=True, read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    subscription = SerializerMethodField(read_only=True)
    price_rub = serializers.SerializerMethodField()

    def get_count_lessons(self, obj):
        return Lesson.objects.filter(name_course=obj).count()

    def get_subscription(self, course):
        return Subscription.objects.filter(
            course=course, user=self.context["request"].user
        ).exists()

    def get_price_rub(self, course):
        return convert_usd_to_rub(course.price_usd)

    class Meta:
        model = Course
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
