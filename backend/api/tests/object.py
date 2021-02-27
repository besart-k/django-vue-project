name_age_schema = {
    "title": "Simple name and age schema with validation",
    "description": "This form defines custom validation rules checking that the two passwords match.",
    "type": "object",
            "properties": {
                "name": {
                    "title": "Name",
                    "type": "string",
                    "minLength": 3
                },
                "age": {
                    "title": "Age",
                    "type": "number",
                    "minimum": 18
                }
            }
}

year_price_schema = {
    "title": "Year Price",
    "description": "This form defines custom validation rules checking that the two passwords match.",
    "type": "object",
            "properties": {
                "year": {
                    "title": "Year",
                    "type": "number",
                    "minimum": 2000
                },
                "price": {
                    "title": "Price",
                    "type": "number",
                }
            }
}
valid_schema = {
    'name': 'Year and Price',
            'definition': {
                "title": "Year Price",
                "description": "Year Price schema",
                "type": "object",
                "properties": {
                    "year": {
                        "title": "Year",
                        "type": "number",
                        "minimum": 2000
                    },
                    "price": {
                        "title": "Price",
                        "type": "number"
                    }
                }
            }
}
invalid_schema = {
    'name': 'Not valid schema example',
            'definition': {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "id": "http://jsonschema.net",
                "type": "any",
                "properties": {
                    "title": {
                        "id": "http://jsonschema.net/title",
                        "type": "string",
                        "required": True
                    }
                }
            }
}
