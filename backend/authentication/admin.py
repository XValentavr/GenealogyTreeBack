from django.contrib import admin

from authentication.models import UserAccount


# Register your models here.
@admin.register(UserAccount)
class User(admin.ModelAdmin):
    fields = (
        'id', 'email', 'username', 'firstName', 'lastName', 'isActive', 'isStaff', 'isSuperuser', 'last_login',
        'date_joined', "isGenealogist")
    readonly_fields = ('id',)
