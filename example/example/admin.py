from django.contrib import admin

from models import CarBrand, BrandModel, Car


class ModelInlineAdmin(admin.TabularInline):
    model = BrandModel
    extra = 2


class CarBrandAdmin(admin.ModelAdmin):
    inlines = [ModelInlineAdmin, ]


class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'title')
    list_filter = ('brand', )


class CarAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'engine', 'color', 'numberplate')
    list_filter = ('model', )


admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(BrandModel, BrandModelAdmin)
admin.site.register(Car, CarAdmin)
