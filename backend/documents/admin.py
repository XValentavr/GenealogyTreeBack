from django.contrib import admin

from .models import Documents


# Register your models here.
@admin.register(Documents)
class Documents(admin.ModelAdmin):
    fields = ('id', 'url')
    search_fields = ('url',)
