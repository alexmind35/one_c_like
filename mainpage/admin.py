from django.contrib import admin

from.models import Main

@admin.register(Main)
class AdminMain(admin.ModelAdmin):
    list_display = ["headingh1","headingh2", "description","vk_social","fb_social","tw_social","phone"]
