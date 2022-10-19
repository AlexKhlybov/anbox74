from django.contrib import admin
from import_export import resources

from apps.product.models import ProductCategory, Boiler, City, Manufacturer


admin.site.register(City)
admin.site.register(Manufacturer)
admin.site.register(ProductCategory)
admin.site.register(Boiler)


class CityResource(resources.ModelResource):
    class Meta:
        model = City

class ManufacturerResource(resources.ModelResource):
    class Meta:
        model = Manufacturer
        
class ProductCategoryResource(resources.ModelResource):
    class Meta:
        model = ProductCategory

class BoilerResource(resources.ModelResource):
    class Meta:
        model = Boiler
