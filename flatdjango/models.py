from django.db import models

# Create your models here.

class MajorUnit(models.Model):
    image_link = models.CharField(max_length=200, blank=True)
    stock_number = models.CharField(max_length=50)
    mfg = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    model_name = models.CharField(max_length=200)
    store = models.CharField(max_length=50, blank=True)
    quote_level = models.CharField(max_length=10, blank=True)
    msrp_total = models.CharField(max_length=20, blank=True)
    sale_price = models.CharField(max_length=20, blank=True)
    nap = models.CharField(max_length=20, blank=True)
    profit_margin = models.CharField(max_length=20, blank=True)
    brochure = models.CharField(max_length=20, blank=True)
    new_edit_modal = models.CharField(max_length=20, blank=True)
    website_price = models.CharField(max_length=20, blank=True)
    cycle_trader = models.CharField(max_length=20, blank=True)
    location_status = models.CharField(max_length=20, blank=True)
    program = models.CharField(max_length=20, blank=True)
    days_on_floor = models.CharField(max_length=10, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Major Unit'
        verbose_name_plural = 'Major Units'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.year} {self.mfg} {self.model_name} - {self.stock_number}"