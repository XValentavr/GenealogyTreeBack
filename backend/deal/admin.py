from django.contrib import admin

from deal.models import DealWithClient


# Register your models here.
@admin.register(DealWithClient)
class Deal(admin.ModelAdmin):
    model = DealWithClient
    list_display = ['id', 'clientTree', 'date', 'document', 'context', 'genealogistTree', 'is_published']
    list_display_links = ('id',)
    search_fields = ('clientTree',)
    list_editable = ('date', 'document', 'context', 'genealogistTree', 'is_published', 'clientTree',)

    @staticmethod
    def client(obj):
        return obj.client.user.username
