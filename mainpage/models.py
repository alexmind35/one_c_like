from django.db import models

class Main (models.Model):
    headingh1 = models.CharField("Заголовок h1", max_length=50)
    headingh2 = models.CharField("Заголовок h2", max_length=80)
    description = models.TextField("описание")
    vk_social = models.URLField("Ссылка Вконтакте")
    fb_social = models.URLField("Ссылка Facebook")
    tw_social = models.URLField("Ссылка Twitter")
    phone = models.CharField("Телефон", max_length=30)
    logoimg = models.ImageField("логотип", upload_to="mainpage/logo", default="", blank=True)

    class Meta:
        verbose_name = "главная"
        verbose_name_plural = "главная"

    def __str__(self):
        return self.headingh1
