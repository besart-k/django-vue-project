from rest_framework import viewsets

from api.serializers import RiskTypeDefinitionSerializer, RiskTypeDataSerializer
from api.models import RiskTypeDefinition, RiskTypeData


class RiskTypeDefinitionViewSet(viewsets.ModelViewSet):
    queryset = RiskTypeDefinition.objects.all()
    serializer_class = RiskTypeDefinitionSerializer


class RiskTypeDataViewSet(viewsets.ModelViewSet):
    queryset = RiskTypeData.objects.all()
    serializer_class = RiskTypeDataSerializer