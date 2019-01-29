from django.db import models

class Product (models.Model):
    name_product = models.CharField("Название", max_length=50)
    desc_product = models.TextField("Описание")
    img_product = models.ImageField("логотип", upload_to="productpage/image", default="", blank=True)

    class Meta:
        verbose_name = "Продукты и сервисы"
        verbose_name_plural = "Продукты"

