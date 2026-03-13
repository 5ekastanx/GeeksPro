from django.contrib import admin
from .models import Trainee, Role
from apps._common.mixins import TabbedTranslationAdmin
from .translation import *


@admin.register(Trainee)
class TraineeAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name", "email", "phone_number", "date_of_birth")
    search_fields = ("name", "email", "phone_number")
    list_filter = ("date_of_birth",)
    ordering = ("id",)
    list_per_page = 10

    fieldsets = (
        ("Основная информация", {
            "fields": ("name", "email",)
        }),
        ("Контактная информация", {
            "fields": ("phone_number", "address",)
        }),
        ("Дополнительно", {
            "fields": ("date_of_birth",)
        }),
    )


@admin.register(Role)
class RoleAdmin(TabbedTranslationAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)
    ordering = ("id",)