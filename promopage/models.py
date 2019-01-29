from django.db import models

class Promo (models.Model):
    descpromo = models.TextField("Текст акции")
    imgpromo = models.ImageField("логотип", upload_to="promopage/image", default="", blank=True)

    class Meta:
        verbose_name = "акции"
        verbose_name_plural = "акции"
