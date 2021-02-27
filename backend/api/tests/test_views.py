import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from api.models import RiskTypeData, RiskTypeDefinition
from api.serializers import (RiskTypeDefinitionSerializer, RiskTypeDefinitionListSerializer,
                             RiskTypeDefinitionCreateSerializer, RiskTypeDataSerializer, RiskTypeDataListSerializer, RiskTypeDataCreateSerializer)

from api.tests.object import *


client = Client()


class RiskTypesDefinitionsRetrieveEndpointsTest(TestCase):
    """ Test module for risk types definitions endpoints """

    def setUp(self):

        self.name_age_schema = name_age_schema
        self.year_price_schema = year_price_schema
        self.name_age = RiskTypeDefinition.objects.create(
            name="Name And Age", definition=self.name_age_schema)
        self.year = RiskTypeDefinition.objects.create(
            name="Year Schema", definition=self.year_price_schema)

    def test_get_all_risk_types(self):
        response = client.get(reverse('risk-type-definitions-list'))
        risk_types = RiskTypeDefinition.objects.all()
        serializer = RiskTypeDefinitionListSerializer(risk_types, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_risk_type(self):
        response = client.get(
            reverse('risk-type-definitions-detail', kwargs={'pk': self.name_age.pk}))
        risk_type = RiskTypeDefinition.objects.get(pk=self.name_age.pk)
        serializer = RiskTypeDefinitionSerializer(risk_type)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_risk_type(self):
        response = client.get(
            reverse('risk-type-definitions-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RiskTypesDefinitionsCreateEndpointsTest(TestCase):
    """ Test module for risk types definitions endpoints """

    def setUp(self):
        self.valid_schema = valid_schema
        self.invalid_schema = invalid_schema

    def test_create_valid_risk_type_definition(self):
        response = client.post(
            reverse('risk-type-definitions-list'),
            data=self.valid_schema,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_risk_type_definition(self):
        response = client.post(
            reverse('risk-type-definitions-list'),
            data=self.invalid_schema,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RiskTypesDefinitionsNotAllowedMethodsTest(TestCase):

    def setUp(self):
        self.name_age_schema = name_age_schema
        self.name_age = RiskTypeDefinition.objects.create(
            name="Name And Age", definition=self.name_age_schema)

    def test_risk_type_definition_update(self):
        response = client.put(
            reverse('risk-type-definitions-detail',
                    kwargs={'pk': self.name_age.pk}),
            data=valid_schema,
            content_type='application/json'
        )
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_risk_type_definition_delete(self):
        response = client.delete(
            reverse('risk-type-definitions-detail',
                    kwargs={'pk': self.name_age.pk}),
            data=valid_schema,
            content_type='application/json'
        )
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class RiskTypesDataRetrieveEndpointsTest(TestCase):
    """ Test module for risk types definitions endpoints """

    def setUp(self):

        self.name_age_schema = name_age_schema
        self.name_age = RiskTypeDefinition.objects.create(
            name="Name And Age", definition=self.name_age_schema)
        self.name_age_data = RiskTypeData.objects.create(
            risk_type_definition=self.name_age, data=name_age_form_data
        )
        self.name_age_data_2 = RiskTypeData.objects.create(
            risk_type_definition=self.name_age, data=name_age_form_data_2
        )

    def test_get_all_risk_types_data(self):
        response = client.get(reverse('risk-type-data-list'))
        risk_types = RiskTypeData.objects.all()
        serializer = RiskTypeDataListSerializer(risk_types, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_risk_type_data(self):
        response = client.get(
            reverse('risk-type-data-detail', kwargs={'pk': self.name_age.pk}))
        risk_type = RiskTypeData.objects.get(pk=self.name_age.pk)
        serializer = RiskTypeDataSerializer(risk_type)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_risk_type(self):
        response = client.get(
            reverse('risk-type-data-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RiskTypesDataCreateEndpointsTest(TestCase):
    """ Test module for risk types definitions endpoints """

    def setUp(self):
        self.name_age_schema = name_age_schema
        self.name_age = RiskTypeDefinition.objects.create(
            name="Name And Age", definition=self.name_age_schema)
        self.name_age_valid_data = {
            'risk_type_definition': self.name_age.pk,
            'data': name_age_form_data
        }
        self.name_age_invalid_data = {
            'risk_type_definition': self.name_age.pk,
            'data': name_age_invalid_form_data
        }

    def test_create_valid_risk_type_data(self):
        response = client.post(
            reverse('risk-type-data-list'),
            data=self.name_age_valid_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_risk_type_data(self):
        response = client.post(
            reverse('risk-type-data-list'),
            data=self.name_age_invalid_data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class RiskTypesDataNotAllowedMethodsTest(TestCase):

    def setUp(self):
        self.name_age_schema = name_age_schema
        self.name_age = RiskTypeDefinition.objects.create(
            name="Name And Age", definition=self.name_age_schema)
        self.name_age_data = RiskTypeData.objects.create(
            risk_type_definition=self.name_age, data=name_age_form_data
        )

    def test_risk_type_data_update(self):
        response = client.put(
            reverse('risk-type-data-detail',
                    kwargs={'pk': self.name_age_data.pk}),
            data={},
            content_type='application/json'
        )
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_risk_type_data_delete(self):
        response = client.delete(
            reverse('risk-type-data-detail',
                    kwargs={'pk': self.name_age.pk}),
            data={},
            content_type='application/json'
        )
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)