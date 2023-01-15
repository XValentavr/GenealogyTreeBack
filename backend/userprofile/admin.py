from django.contrib import admin

from userprofile.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    model = UserProfile
    list_display = (
        'id', 'getName', 'dateOfBirth', 'avatar', 'telegram', 'facebook', 'whatsapp', 'twitter', 'linkedin',)
    list_display_links = ('id', 'getName')
    search_fields = ('get_name',)
    list_editable = ('dateOfBirth', 'avatar', 'telegram', 'facebook', 'whatsapp', 'twitter', 'linkedin',)

    @staticmethod
    def getName(obj):
        return obj.user.username
