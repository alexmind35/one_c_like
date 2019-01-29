from django.contrib import admin

from.models import Client

@admin.register(Client)
class AdminClient(admin.ModelAdmin):
    list_display = ["name_client","logo_client"]

