import jsonschema, json

# Define a JSON schema.
schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname" : {"type": "string"},
        "age": {"type": "integer"}
    },
    "required": ["firstname", "lastname", "age"]
}

#JSON document
document = {"firstname" : "ABC",
            "lastname" : "XYZ",
            "age" : "12",
            "hobbies" : "Reading"
            }

try:
    jsonschema.validate(document, schema)
except jsonschema.exceptions.ValidationError as x:
    print(x)
                       

# demonstrate age validation
# demonstrate "required"