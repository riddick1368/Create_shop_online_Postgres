
from django.contrib import admin
from .models import Product,Category,Brand,Varations,ProductFeautre,ProductImage

# Register your models here.
class ProductCustomize(admin.ModelAdmin):
    model = Product
    list_display = ['title','brand','active','price']
    list_filter = ['title','brand','category','active']
    list_per_page = 15
    list_filter = ['title','brand','category']
    list_display_links = ['title']
    list_editable = ['brand']


    class Meta:
        order_by = ['-title']


class CategoryCustomize(admin.ModelAdmin):
    model = Category
    list_display = ['title', 'slug']
    list_filter = ['category' ]
    list_per_page = 15
    list_filter = ['title']
    list_display_links = ['title']
    class Meta:
        order_by = ['-title']



admin.site.register(Product,ProductCustomize)
admin.site.register(Category,CategoryCustomize)
admin.site.register(Brand)
admin.site.register(ProductFeautre)
admin.site.register(Varations)
admin.site.register(ProductImage)