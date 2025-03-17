from django.contrib import admin
from .models import Chiroq

# Register your models here.

class ChiroqAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'price', 'quantity')
    search_fields = ('brand', 'price', 'quantity')
    list_filter = ('price','quantity')

admin.site.register(Chiroq, ChiroqAdmin)