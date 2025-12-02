import xml.etree.ElementTree as ET
xml_data = '''
<libro>
<titolo>Il Grande Gatsby</titolo>
<autore>F. Scott Fitzgerald</autore>
<anno>1925</anno>
</libro>
'''
root = ET.fromstring(xml_data)
print(type(root))
print("Titolo:", root.find('titolo').text)