from django.contrib import admin

from .models import Document, TypeConsumables, TypeEquipment, Consumables, Equipment, ActionField, ProcedureTemplate, Procedure, Sample, Analysis

admin.site.register(Document)
admin.site.register(TypeConsumables)
admin.site.register(TypeEquipment)
admin.site.register(Consumables)
admin.site.register(Equipment)
admin.site.register(ActionField)
admin.site.register(ProcedureTemplate)
admin.site.register(Procedure)
admin.site.register(Sample)
admin.site.register(Analysis)

