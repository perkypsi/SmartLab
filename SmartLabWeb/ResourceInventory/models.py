from django.db import models
from AccessManagementSystem.models import Profile, Role, Project, Enviroment
from LabManagementProcess.models import StorageLocation

class Document(models.Model):
    name = models.CharField('Название документа', max_length=200, null=False)
    description = models.TextField('Описание документа', max_length=10000, null=False)
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

class TypeConsumables(models.Model):
    name = models.CharField('Название типа расходника', max_length=200, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип расходника'
        verbose_name_plural = 'Типы расходников'

class TypeEquipment(models.Model):
    name = models.CharField('Название типа оборудования', max_length=200, null=False)
    description = models.TextField('Описание поля действия', max_length=10000, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'

class Consumables(models.Model):
    name = models.CharField('Название расходника', max_length=200, null=False)
    description = models.TextField('Описание расходника', max_length=10000, null=False)
    type = models.ForeignKey(TypeConsumables, verbose_name="Тип расходника", on_delete=models.PROTECT, related_name='consumables', null=False)
    storage_location = models.ForeignKey(StorageLocation, verbose_name="Местоположение", on_delete=models.PROTECT, related_name='consumables', null=False)
    production_date = models.DateField('Дата изготовления', null=True)
    storage_life = models.DateField('Срок годности', null=True)
    amount = models.FloatField('Остаток', blank=True)
    usage_rights = models.ManyToManyField(Role, related_name='rights_consumables', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Расходник'
        verbose_name_plural = 'Расходники'

class Equipment(models.Model):
    name = models.CharField('Название оборудования', max_length=200, null=False)
    description = models.TextField('Описание оборудования', max_length=10000, null=False)
    type = models.ForeignKey(TypeEquipment, verbose_name="Тип оборудования", on_delete=models.PROTECT, related_name='equipments', null=False)
    storage_location = models.ForeignKey(StorageLocation, verbose_name="Местоположение", on_delete=models.PROTECT, related_name='equipments', null=False)
    usage_rights = models.ManyToManyField(Role, related_name='rights_equipments', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'

class ActionField(models.Model):
    name = models.CharField('Название поля действия', max_length=200, null=False)
    description = models.TextField('Описание поля действия', max_length=10000, null=False)
    equipments = models.ManyToManyField(Equipment, related_name='action_fields', blank=True)
    consumables = models.ManyToManyField(Consumables, related_name='action_fields', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поле действия'
        verbose_name_plural = 'Поля действия'


class ProcedureTemplate(models.Model):
    name = models.CharField('Название поля действия', max_length=200, null=False)
    description = models.TextField('Описание поля действия', max_length=10000, null=False)
    action_fields = models.ManyToManyField(ActionField, related_name='procedure_templates', blank=True)
    author = models.ForeignKey(Enviroment, verbose_name="Автор", on_delete=models.PROTECT, related_name='procedure_templates', null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Шаблон методики'
        verbose_name_plural = 'Шаблоны методик'

class Procedure(models.Model):
    name = models.CharField('Название анализа', max_length=200, null=False)
    description = models.TextField('Описание анализа', max_length=10000, null=False)
    created_date = models.DateTimeField("Дата рождения пользователя", auto_now_add=True)
    author = models.ForeignKey(Enviroment, verbose_name="Автор", on_delete=models.PROTECT, related_name='procedures', null=False)
    template = models.ForeignKey(ProcedureTemplate, verbose_name="Шаблон", on_delete=models.PROTECT, related_name='procedures', null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Методика'
        verbose_name_plural = 'Методики'

class Sample(models.Model):
    name = models.CharField('Название образца', max_length=200, null=False)
    description = models.TextField('Описание образца', max_length=10000, null=False)
    storage_location = models.ForeignKey(StorageLocation, verbose_name="Местоположение", on_delete=models.PROTECT, related_name='samples', null=False)
    production_date = models.DateField('Дата изготовления', null=True)
    author = models.ForeignKey(Profile, verbose_name="Автор", on_delete=models.PROTECT, related_name='samples', null=False)
    usage_rights = models.ManyToManyField(Role, related_name='samples', blank=True)
    procedure = models.ForeignKey(Procedure, verbose_name="Методика", on_delete=models.PROTECT, related_name='samples', null=False)
    amount = models.FloatField('Остаток', blank=True)
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.PROTECT, related_name='samples', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Образец'
        verbose_name_plural = 'Образцы'

class Analysis(models.Model):
    name = models.CharField('Название анализа', max_length=200, null=False)
    description = models.TextField('Описание анализа', max_length=10000, null=False)
    documents = models.ManyToManyField(Document, related_name='analysis', blank=True)
    equipments = models.ForeignKey(Equipment, verbose_name="Оборудование", on_delete=models.DO_NOTHING, related_name='analysis')
    executor = models.ForeignKey(Profile, verbose_name="Исполнитель", on_delete=models.DO_NOTHING, related_name='analysis')
    sample = models.ForeignKey(Sample, verbose_name="Образец", on_delete=models.DO_NOTHING, related_name='analysis', null=True)
    consumables = models.ForeignKey(Consumables, verbose_name="Расходник", on_delete=models.DO_NOTHING, related_name='analysis', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'