from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    pay_list = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("__all__")
