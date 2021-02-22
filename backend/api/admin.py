from django.contrib import admin
from api.models import RiskTypeDefinition, RiskTypeData

admin.site.register(RiskTypeData)
admin.site.register(RiskTypeDefinition)