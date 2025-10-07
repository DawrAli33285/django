from django.contrib import admin
from .models import MajorUnit

@admin.register(MajorUnit)
class MajorUnitAdmin(admin.ModelAdmin):
    list_display = ['stock_number', 'mfg', 'year', 'model_name', 'sale_price', 'days_on_floor']
    list_filter = ['mfg', 'year', 'store']
    search_fields = ['stock_number', 'model_name', 'mfg']