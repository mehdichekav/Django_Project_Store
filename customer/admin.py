from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationForm, UserChangeForm
from .models import User, Address


# admin.site.register(Register)
# admin.site.register(Edit_Customer)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = [
        (None, {'fields': ('first_name', 'last_name', 'password')}),
        ('personal info', {'fields': ('is_active',)}),
        ('permissions', {'fields': ('is_admin',)})
    ]
    add_fieldsets = [
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')
        }),
    ]
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Address)