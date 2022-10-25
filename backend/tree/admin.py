from django.contrib import admin

from tree.models import MainRootUser, FemaleLine, MaleLine


# Register your models here.
@admin.register(MainRootUser)
class MainRootUserAdmin(admin.ModelAdmin):
    """
    Represents root user into admin page
    """
    model = MainRootUser
    list_display = (
        'id', 'get_first_name', 'get_lastname', 'surname', 'mother_surname', 'date_of_birth', 'place_of_birth',
        'date_of_marry', 'unique_root')

    list_display_links = ('id',)

    search_fields = ('get_first_name', 'date_of_birth', 'surname')

    list_editable = ('surname', 'mother_surname',
                     'date_of_birth', 'place_of_birth',
                     'date_of_marry',)

    readonly_fields = ('unique_root',)

    @staticmethod
    def get_first_name(obj):
        return obj.user.username

    @staticmethod
    def get_lastname(obj):
        return obj.user.last_name


@admin.register(FemaleLine)
class FemaleLineAdmin(admin.ModelAdmin):
    """
    Represent FemaleLine into admin page
    """
    model = FemaleLine
    list_display = (
        'id', 'root', 'first_name', 'surname', 'last_name', 'mother_surname', 'date_of_birth', 'place_of_birth',
        'date_of_marry', 'date_of_marry', 'date_of_death', 'document', 'is_published', 'unique_female')

    list_display_links = ('id',)

    search_fields = ('first_name', 'date_of_birth', 'surname', 'place_of_birth')

    list_editable = ('first_name', 'surname', 'last_name', 'mother_surname', 'date_of_birth', 'place_of_birth',
                     'date_of_marry', 'date_of_marry', 'date_of_death', 'document', 'is_published',)

    readonly_fields = ('unique_female',)


@admin.register(MaleLine)
class MaleLineAdmin(admin.ModelAdmin):
    """
    Represents MaleLine into admin page
    """
    model = MaleLine
    list_display = (
        'id', 'root', 'first_name', 'surname', 'last_name', 'mother_surname', 'date_of_birth', 'place_of_birth',
        'date_of_marry', 'date_of_marry', 'date_of_death', 'document', 'is_published', 'unique_male')

    list_display_links = ('id',)

    search_fields = ('first_name', 'date_of_birth', 'surname', 'place_of_birth')

    list_editable = ('first_name', 'surname', 'last_name', 'mother_surname', 'date_of_birth', 'place_of_birth',
                     'date_of_marry', 'date_of_marry', 'date_of_death', 'document', 'is_published',)

    readonly_fields = ('unique_male',)
