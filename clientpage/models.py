from django.db import models

class Client (models.Model):
    name_client = models.CharField("Название", max_length=50)
    logo_client = models.ImageField("Фотография", upload_to="clientpage/logo", default="", blank=True)

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"
