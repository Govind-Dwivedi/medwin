from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name')
    list_filter = ('is_patient', 'is_doctor', 'is_administrator')
    fieldsets = (
        (None, {
            "fields": ('email','password')
        }),
        ("Personal Info", {
            "fields": ('first_name',)
        }),
        ("Permissions", {
            "fields": (
                'is_active',
                'is_staff',
                'is_admin',
                'is_superuser',
                'is_patient',
                'is_doctor',
                'is_administrator'
            )
        })
    )
    
    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": ('email', 'password1', 'password2')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
# Register your models here.
