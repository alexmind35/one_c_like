from django.contrib import admin

from.models import Team

@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
    list_display = ["fio_team","work_team","vk_team","fb_team","tw_team","photo_team"]
