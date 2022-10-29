from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Farmer, Merchant


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ["email", "username", "user_role"]
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'user_role',
                )
            }
        )
    )


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Merchant)
admin.site.register(Farmer)
