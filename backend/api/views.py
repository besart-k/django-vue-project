from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import RiskTypeDefinition, RiskTypeData
from api.serializers import (RiskTypeDefinitionSerializer, RiskTypeDefinitionListSerializer,
                             RiskTypeDefinitionCreateSerializer, RiskTypeDataSerializer, RiskTypeDataListSerializer, RiskTypeDataCreateSerializer)


class RiskTypeDefinitionViewSet(viewsets.ModelViewSet):
    queryset = RiskTypeDefinition.objects.all()
    serializer_class = RiskTypeDefinitionSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = RiskTypeDefinitionListSerializer
        return super(RiskTypeDefinitionViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = RiskTypeDefinitionCreateSerializer
        return super(RiskTypeDefinitionViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class RiskTypeDataViewSet(viewsets.ModelViewSet):
    queryset = RiskTypeData.objects.all()
    serializer_class = RiskTypeDataSerializer

    def list(self, request, *args, **kwargs):
        self.serializer_class = RiskTypeDataListSerializer
        return super(RiskTypeDataViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = RiskTypeDataCreateSerializer
        return super(RiskTypeDataViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
