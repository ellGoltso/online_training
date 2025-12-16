from rest_framework import serializers

from users.models import Payment, User, Subscription


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "phone_number", "city", "avatar")


class SubscriptionSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = "__all__"

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        course = obj.course_subscription
        return Subscription.objects.filter(
            user_subscription=user, course_subscription=course
        ).exists()
