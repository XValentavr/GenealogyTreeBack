from django.contrib import admin

from userprofile.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    model = UserProfile
    list_display = (
        'id', 'get_name', 'date_of_birth', 'avatar', 'telegram', 'facebook', 'whatsapp', 'twitter', 'linkedin',)
    list_display_links = ('id', 'get_name')
    search_fields = ('get_name',)
    list_editable = ('date_of_birth', 'avatar', 'telegram', 'facebook', 'whatsapp', 'twitter', 'linkedin',)

    @staticmethod
    def get_name(obj):
        return obj.user.username
