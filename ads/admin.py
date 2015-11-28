from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
	pass
admin.site.register(Item, ItemAdmin)

class CategoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(Category, CategoryAdmin)

class LocationAdmin(admin.ModelAdmin):
	pass
admin.site.register(Location, LocationAdmin)