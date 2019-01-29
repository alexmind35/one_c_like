from django.db import models

class Team (models.Model):
    fio_team = models.CharField("Имя и фамилия", max_length=50)
    work_team = models.CharField("Должность", max_length=50)
    vk_team = models.URLField("Ссылка Вконтакте")
    fb_team = models.URLField("Ссылка Facebook")
    tw_team = models.URLField("Ссылка Twitter")
    photo_team = models.ImageField("Фотография", upload_to="teampage/photo", default="", blank=True)

    class Meta:
        verbose_name = "Команда.Кто мы?"
        verbose_name_plural = "команда"