class BaseModel(models.Model):
    created_by = ForeignKey
    updated_by = ForeignKey
    created_date = DateTimeField
    modified_date = DateTimeField

class RiskTypeDefinition(BaseModel):
    id = AutoField
    name = CharField
    definition = JSONField

class RiskTypeData(BaseModel):
    id = AutoField
    risk_type_definition = ForeignKey to RiskTypeDefinition
    data = JSONField
