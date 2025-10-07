from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_csv, name='upload_csv'),
    path('process-csv/', views.process_csv, name='process_csv'),
    path('view-units/', views.view_units, name='view_units'),
]