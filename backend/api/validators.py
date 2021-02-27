from django.core.exceptions import ValidationError
from jsonschema import (validate, Draft4Validator,
                        SchemaError, draft4_format_checker, ValidationError as SchemaValidationError)


def validate_schema(schema):
    try:
        Draft4Validator.check_schema(schema)
    except SchemaError as SE:
        raise ValidationError(SE)


def validate_data_with_schema(data, schema):
    try:
        validate(instance=data, schema=schema,
                 format_checker=draft4_format_checker)
    except SchemaValidationError as SVE:
        raise ValidationError(SVE)
