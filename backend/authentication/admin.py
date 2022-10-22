from django.contrib import admin

from authentication.models import UserAccount


# Register your models here.
@admin.register(UserAccount)
class User(admin.ModelAdmin):
    fields = ('email', 'username', 'is_active', 'is_staff', 'is_superuser', 'uid', 'last_login', 'date_joined')
    readonly_fields = ('uid',)
