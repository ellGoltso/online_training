from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_link_video
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    link_video = serializers.CharField(
        required=False, allow_null=True, validators=[validate_link_video]
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_count_lessons(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        course = obj
        return Subscription.objects.filter(
            user_subscription=user, course_subscription=course
        ).exists()
