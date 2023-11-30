from django.contrib import admin
from app_cof.models import Coffee

# Register your models here.

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','is_premium','promotion_end_at']
    search_fields = ['title']
    list_filter = ['is_premium']

admin.site.register(Coffee,CoffeeAdmin)
