from rest_framework import viewsets, status

from api.serializers import RiskTypeDefinitionSerializer, RiskTypeDataSerializer
from api.models import RiskTypeDefinition, RiskTypeData


class RiskTypeDefinitionViewSet(viewsets.ModelViewSet):
    queryset = RiskTypeDefinition.objects.all()
    serializer_class = RiskTypeDefinitionSerializer

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

    def destroy(self, request, pk=None):
        response = {'message': 'Delete function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        response = {'message': 'Update function is not offered in this path.'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)
