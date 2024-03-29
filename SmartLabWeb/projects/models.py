from django.db import models
from employees.models import employee

class Project(models.Model):
    project_name = models.CharField('Название проекта', max_length = 255)
    description_template = models.TextField("Описание проекта")
    member = models.ManyToManyField(employee)
    leader = models.ManyToManyField(employee)
    create_date = models.DateTimeField('Дата создания')