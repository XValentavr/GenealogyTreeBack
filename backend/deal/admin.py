from django.contrib import admin

from deal.models import DealWithClient


# Register your models here.
@admin.register(DealWithClient)
class Deal(admin.ModelAdmin):
    model = DealWithClient
    list_display = ['id', 'client', 'date', 'document', 'context', 'genealog', 'is_published']
    list_display_links = ('id',)
    search_fields = ('client',)
    list_editable = ('date', 'document', 'context', 'genealog', 'is_published','client', )

    @staticmethod
    def client(obj):
        return obj.client.user.username
