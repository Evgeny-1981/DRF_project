from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "phone",
        "country",
    )
    list_filter = ("email",)
    search_fields = (
        "email",
        "phone",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "data_payment",
        "paid_course",
        "paid_lesson",
        "payment_method",
    )
    list_filter = ("data_payment",)
    search_fields = (
        "data_payment",
        "payment_method",
    )
