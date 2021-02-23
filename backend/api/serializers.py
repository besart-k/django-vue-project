from rest_framework import serializers

from api.models import RiskTypeData, RiskTypeDefinition


class RiskTypeDefinitionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskTypeDefinition
        fields = ('id', 'name')

class RiskTypeDefinitionDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskTypeDefinition
        fields = ('id', 'name', 'definition')


class RiskTypeDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskTypeData
        fields = ('risk_type_definition', 'data')

    def validate(self, attrs):
        instance = RiskTypeData(**attrs)
        instance.clean()
        return attrs
