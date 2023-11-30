from django.contrib import admin
from app_gen.models import Subscription

# Register your models here.

class SubscritionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','status','registerd_at']
    search_fields = ['name','email']
    list_filter = ['status']

admin.site.register(Subscription,SubscritionAdmin)