from django.contrib import admin
from . import models
from django.contrib.auth.models import User, Group

admin.site.unregister(Group)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ['id','name','image','created_at']
    search_fields = ['name']
    list_filter = ['name']
    list_editable = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','category','description','offer_price','price']
    search_fields = ['name']
    list_filter = ['category']
    list_editable = ['description','name','price','offer_price']
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id','main_title','sub_title','image','url']
    list_editable = ['main_title','sub_title','image']

# Register your models here.
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Slider,SliderAdmin)
admin.site.register(models.Favourite)
admin.site.register(models.Size)
admin.site.register(models.Color)
admin.site.register(models.Sku)