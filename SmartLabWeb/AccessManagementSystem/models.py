from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class Enviroment(models.Model):
    name = models.CharField('Название окружения', max_length=200)
    description = models.TextField('Описание окружения', max_length=10000)

    def __str__(self):
        return self.profile.username

    class Meta:
        verbose_name = 'Окружение'
        verbose_name_plural = 'Окружения'


class AccessLevel(models.Model):
    name = models.CharField('Название роли', max_length=200)
    enviroment = models.ForeignKey(Enviroment, verbose_name="Окружение", related_name='access_levels', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Уровень доступа'
        verbose_name_plural = 'Уровни доступа'


class Role(models.Model):
    name = models.CharField('Название роли', max_length=200)
    description = models.TextField('Описание роли', max_length=10000)
    access_level = models.ForeignKey(AccessLevel, verbose_name="Уровень доступа", related_name='roles', on_delete=models.PROTECT)
    enviroment = models.ForeignKey(Enviroment, verbose_name="Окружение", related_name='roles', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Profile(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='profile_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='profile_user_permissions')
    patronymic = models.CharField("Отчество пользователя", max_length=100)
    birthdate = models.DateField("Дата рождения пользователя")
    phone_number = models.CharField("Номер телефона", max_length=20)
    role = models.ManyToManyField(Role, related_name='role', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Project(models.Model):
    name = models.CharField('Название проекта', max_length=200, null=False)
    description = models.TextField('Описание проекта', max_length=10000, null=False)
    participants = models.ManyToManyField(Profile, related_name='participating_projects', blank=True)
    leader = models.ForeignKey(Profile, verbose_name="Участники", on_delete=models.PROTECT, related_name='leading_projects', null=False)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Notification(models.Model):
    title = models.CharField('Заголовок увеомления', max_length=200, null=False)
    description = models.TextField('Содержание уведомления', max_length=10000, null=False)
    leader = models.ForeignKey(Profile, verbose_name="Получатель", related_name='notifications', on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

