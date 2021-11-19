from django.contrib import admin
from .models import *


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Mortgage)
class MortgageAdmin(admin.ModelAdmin):
    pass


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    pass


@admin.register(Renovation_costs)
class Renovation_costsAdmin(admin.ModelAdmin):
    pass


@admin.register(Attributes)
class AttributesAdmin(admin.ModelAdmin):
    pass
