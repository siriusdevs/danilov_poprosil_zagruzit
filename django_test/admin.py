from django.contrib import admin

from .models import Person, Equipment


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    model = Person

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    model = Equipment