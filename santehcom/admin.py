from django.contrib import admin

from santehcom.models import *

admin.site.register(Profile)
admin.site.register(Favourite)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Score)
admin.site.register(Crate)
admin.site.register(Rating)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created']
    list_filter = ['available', 'created']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
