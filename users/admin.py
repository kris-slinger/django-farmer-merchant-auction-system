from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Farmer, Merchant
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ["email", "username"]

    fieldsets = (
        (None, {'fields': ('email', 'username', 'user_national_id', 'user_phone',)}),
        ('Permissions', {'fields': ('user_role',
         'is_staff', 'is_superuser', 'is_active')}),
    )



# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Merchant)
admin.site.register(Farmer)


admin.site.site_header = 'Slinger admin page'
admin.site.site_title = 'Slinger admin page'
