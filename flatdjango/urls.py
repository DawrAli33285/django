from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Existing routes
    path('', views.upload_csv, name='upload_csv'),
    path('process-csv/', views.process_csv, name='process_csv'),
    path('view-units/', views.view_units, name='view_units'),
    
    # New routes for all pages
    path('landing/', views.landing_page, name='landing_page'),
    path('login/', views.login_page, name='login_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('commission/', views.commission, name='commission'),
    path('contact/', views.contact, name='contact'),
    path('coupons/', views.coupons, name='coupons'),
    path('cycle-trade-units/', views.cycle_trade_units, name='cycle_trade_units'),
    path('major-units-grid/', views.major_units_grid, name='major_units_grid'),
    path('mu-missing/', views.mu_missing, name='mu_missing'),
    path('quotes/', views.quotes, name='quotes'),
    path('sale-programs/', views.sale_programs, name='sale_programs'),
]