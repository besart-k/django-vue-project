from rest_framework import serializers

from api.models import RiskTypeData, RiskTypeDefinition


class RiskTypeDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypeDefinition
        fields = ('id', 'name', 'definition')


class RiskTypeDefinitionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypeDefinition
        fields = ('id', 'name')


class RiskTypeDefinitionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypeDefinition
        fields = ('name', 'definition')

    def validate(self, attrs):
        instance = RiskTypeDefinition(**attrs)
        instance.clean()
        return attrs


class RiskTypeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypeData
        fields = ('id', 'risk_type_definition', 'data')


class RiskTypeDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypeData
        fields = ('id', 'risk_type_definition')


class RiskTypeDataCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskTypeData
        fields = ('risk_type_definition', 'data')

    def validate(self, attrs):
        instance = RiskTypeData(**attrs)
        instance.clean()
        return attrs
