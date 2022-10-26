from django.contrib import admin

from .models import Support


# Register your models here.
@admin.register(Support)
class TechSupport(admin.ModelAdmin):
    fields = ('name', 'date', 'email', 'phone')
    search_fields = ('name', 'date', 'email', 'phone')
