from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserType
from django.utils.translation import to_locale, get_language, ugettext_lazy as _

@admin.register(User)
class MyUserAdmin(UserAdmin):
	fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name',  'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )



@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
	pass