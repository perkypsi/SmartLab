from django.db import models

class employee(models.Model):
    fullname = models.CharField("Фамилия")
