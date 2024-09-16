import json


class Person:
    def __init__(self, name, age, cf):
        self.name = name
        self.age = age
        self.cf = cf


class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "age": obj.age, "Codice fscale": obj.cf}
        return super().default(obj)


# Create a custom object
person = Person("Ashutosh Krishna", 23, "JHDO3445ksj12")

# Encode the custom object using the custom encoder
json_str = json.dumps(person, cls=PersonEncoder)

# Print the encoded JSON string
print(json_str)