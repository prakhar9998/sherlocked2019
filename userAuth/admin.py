from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Player

class PlayerResource(resources.ModelResource):

    class Meta:
        model = Player
        fields = ('id', 'username', 'email', 'zeal_Id', 'contact_no', 'college_name',)

class PlayerAdmin(ImportExportModelAdmin):
    resource_class = PlayerResource

admin.site.register(Player, PlayerAdmin)
