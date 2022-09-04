from django.contrib import admin
from .models import Tarifs, Training, Clubs, Personal
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

@admin.register(Tarifs)
class tarif(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Training)
class trainin(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Clubs)
class club(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True

@admin.register(Personal)
class person(ImportExportModelAdmin, SimpleHistoryAdmin):
    class Meta:
        proxy = True
