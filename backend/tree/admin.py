from django.contrib import admin

from tree.models import MainRootUser, FemaleLine, MaleLine


# Register your models here.
@admin.register(MainRootUser)
class MainRootUserAdmin(admin.ModelAdmin):
    """
    Represents root user into admin page
    """
    model = MainRootUser
    list_display = ('id', 'rootUser', 'anyInfo', 'buildsBy')

    list_display_links = ('id', 'rootUser', 'anyInfo', 'buildsBy')

    search_fields = ('id', 'rootUser', 'anyInfo', 'buildsBy')

    readonly_fields = ('id',)


@admin.register(FemaleLine)
class FemaleLineAdmin(admin.ModelAdmin):
    """
    Represent FemaleLine into admin page
    """
    model = FemaleLine
    list_display = ('id', 'root', 'anyInfo', 'prevAncestor',)

    list_display_links = ('id',)

    search_fields = ('id', 'root', 'anyInfo', 'prevAncestor',)

    readonly_fields = ('id',)


@admin.register(MaleLine)
class MaleLineAdmin(admin.ModelAdmin):
    """
    Represents MaleLine into admin page
    """
    model = MaleLine
    list_display = ('id', 'root', 'anyInfo', 'prevAncestor')

    list_display_links = ('id',)

    search_fields = ('id', 'root', 'anyInfo', 'prevAncestor')

    readonly_fields = ('id',)
