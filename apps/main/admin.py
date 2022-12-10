from django.contrib import admin
from import_export import resources
from solo.admin import SingletonModelAdmin
from apps.main.models import SiteConfiguration, Delivery


admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(Delivery)

class ConfigResource(resources.ModelResource):
    class Meta:
        model = SiteConfiguration

class DeliveryResource(resources.ModelResource):
    class Meta:
        model = Delivery
