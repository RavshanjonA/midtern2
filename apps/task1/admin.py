from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm, LoginForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["phone_number", "is_staff", "is_active"]
    list_filter = ["phone_number", "is_staff", "is_active"]
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("Details", {"fields": ("first_name", "last_name", "is_deleted")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Details",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
    )
    search_fields = ("phone_number",)
    ordering = ("-created_at",)


admin.site.register(User, CustomUserAdmin)

admin.site.login_form = LoginForm
admin.site.login_template = "login.html"
