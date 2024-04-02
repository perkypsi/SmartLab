from django.db import models
from AccessManagementSystem.models import Profile, Enviroment

class Lab(models.Model):
    name = models.CharField('Название лаборатории', max_length=200, null=False)
    description = models.TextField('Описание лаборатории', max_length=10000, null=False)
    profiles = models.ManyToManyField(Profile, related_name='labs', blank=True)
    enviroment =  models.ForeignKey(Enviroment, verbose_name="Окружение", on_delete=models.PROTECT, related_name='labs', null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатории'


class StorageLocation(models.Model):
    name = models.CharField('Название документа', max_length=200, null=False)
    lab = models.ForeignKey(Lab, verbose_name="Лаборатория", on_delete=models.PROTECT, related_name='storage_locations', null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'
