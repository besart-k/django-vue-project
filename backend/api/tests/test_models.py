from django.test import TestCase
from api.models import RiskTypeDefinition
from django.core.exceptions import ValidationError


class RiskTypeDefinitionTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        schema_example = {
            "title": "Simple address form field",
            "description": "Simple address form field",
            "type": "object",
            "required": [
                "address"
            ],
            "properties": {
                "address": {
                    "type": "string",
                    "title": "Address",
                    "minLength": 5
                }
            }
        }
        RiskTypeDefinition.objects.create(
            name="Address", definition=schema_example)

    def test_schema_access(self):
        risk_type = RiskTypeDefinition.objects.get(name="Address")
        definition = risk_type.definition
        self.assertEqual(definition['properties']['address']['type'], "string")
        self.assertEqual(definition['required'], ["address"])
