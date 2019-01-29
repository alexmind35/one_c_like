from django.contrib import admin

from.models import Promo

@admin.register(Promo)
class AdminPromo(admin.ModelAdmin):
    list_display = ["descpromo","imgpromo"]
