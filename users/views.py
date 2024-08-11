from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import Payment, User
from users.permissions import IsOwnerProfile
from users.serilazers import PaymentSerializer, UserSerializer
from users.services import choose_material
from users.services import (
    create_stripe_price,
    create_stripe_product,
    create_stripe_session,
)


class UserCreateAPIView(generics.CreateAPIView):
    """Класс для создания пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Класс для просмотра пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Класс для обновления пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsOwnerProfile,
    )


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для просмотра конкретного пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)


class UserDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления конкретного пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)


class PaymentListAPIView(generics.ListAPIView):
    """Класс для просмотра платежей"""

    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ("paid_course", "paid_lesson", "payment_method")
    ordering_fields = ("data_payment",)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        """Сохраняет платеж и создает сессию в страйпе для безналичной оплаты"""

        payment = serializer.save(user=self.request.user)
        material = choose_material(payment)
        if payment.payment_method == "Банковский перевод":
            # Создание платежа в страйпе при безналичной оплате.
            product = create_stripe_product(material)
            price = create_stripe_price(payment.summ_payment, product)
            session_id, payment_link = create_stripe_session(price, payment.pk)
            payment.session_id = session_id
            payment.payment_link = payment_link
            payment.summ_payment = price.unit_amount / 100
            payment.save()
        else:
            payment.save()
