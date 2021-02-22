from django.db import models
from django.conf import settings
from jsonschema import validate


class BaseModel(models.Model):
    # TODO: Remove null=True and link with request user if needed
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   null=True, blank=True,related_name='%(app_label)s_%(class)s_created_by')
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   null=True, blank=True,related_name='%(app_label)s_%(class)s_updated_by')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RiskTypeDefinition(BaseModel):
    id = models.AutoField(db_column="Id", primary_key=True)
    name = models.CharField(db_column="Name", max_length=50, unique=True)
    definition = models.JSONField()

    class Meta:
        db_table = 'RiskTypesDefinitions'
        managed = True
        verbose_name = 'Risk Definition'
        verbose_name_plural = 'Risk Definitions'

    def __str__(self):
        return self.name


class RiskTypeData(BaseModel):
    id = models.AutoField(db_column="Id", primary_key=True)
    risk_type_definition = models.ForeignKey(
        RiskTypeDefinition, on_delete=models.CASCADE)
    data = models.JSONField()

    class Meta:
        db_table = 'RiskTypeData'
        managed = True
        verbose_name = 'Risk Type Data'
        verbose_name_plural = 'Risk Types Data'

    def __str__(self):
        return str(self.id)
    
    def clean(self):
        
        validate(instance=self.data, schema=self.risk_type_definition.definition)
