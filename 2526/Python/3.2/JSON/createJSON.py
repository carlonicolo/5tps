import json
json_data = '''
{
"libro": {
"titolo": "Il Grande Gatsby",
"autore": "F. Scott Fitzgerald",
"anno": 1925
}
}
'''
data = json.loads(json_data)
print(type(data))
print("Titolo:", data['libro']['titolo'])