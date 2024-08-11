from rest_framework import serializers

from users.models import Payment, User
from users.services import retrieve_sessions_statuses


class PaymentSerializer(serializers.ModelSerializer):
    payment_status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = "__all__"

    def get_payment_status(self, obj):
        """Получение статуса платежной сессии в Stripe."""

        if obj.session_id is not None:
            return retrieve_sessions_statuses(obj.session_id)
        return "Сессия оплаты завершилась сошибкой"


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(
        source="payment_set",
        read_only=True,
        many=True,
    )

    class Meta:
        model = User
        fields = "__all__"
