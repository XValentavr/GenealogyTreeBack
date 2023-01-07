from django.contrib import admin

from genealogistBuildsTree.models import GenealogistBuildsTree


# Register your models here.
@admin.register(GenealogistBuildsTree)
class GenealogistBuildTree(admin.ModelAdmin):
    model = GenealogistBuildsTree
    list_display = ['id', 'client', 'isShown', 'genealogist', 'status']
    list_display_links = ('id',)
    search_fields = ('client', 'genealogist')
    list_editable = ('isShown', 'genealogist',)

    @staticmethod
    def client(obj):
        return obj.client.user.username
