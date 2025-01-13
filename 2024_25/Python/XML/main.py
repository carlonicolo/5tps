import xml.etree.ElementTree as ET

# Define the Person class
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, Email: {self.email})"

# Function to parse XML and create a Person object
def parse_person_from_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extract data from the XML elements
    name = root.find('Name').text
    age = int(root.find('Age').text)
    email = root.find('Email').text

    # Create and return a Person object
    return Person(name, age, email)

# Example usage
if __name__ == "__main__":
    # Path to the XML file
    xml_file = "person.xml"

    # Parse the XML file and create a Person object
    person = parse_person_from_xml(xml_file)

    # Print the Person object
    print(person)
