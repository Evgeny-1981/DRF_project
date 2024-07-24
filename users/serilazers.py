from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    pay_list = PaymentSerializer(source="payment_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name",  "last_name", "email", "phone", "pay_list",)
