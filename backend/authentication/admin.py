from django.contrib import admin

from authentication.models import UserAccount


# Register your models here.
@admin.register(UserAccount)
class User(admin.ModelAdmin):
    fields = (
        'id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'last_login',
        'date_joined', "is_genealogist")
    readonly_fields = ('id',)
