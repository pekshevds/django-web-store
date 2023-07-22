from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from auth_app.models import User


class ProfileAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "image")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "preview")

    def preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=50 height=50>')
        return mark_safe('<img src="" width=50 height=50>')


admin.site.register(User, ProfileAdmin)
