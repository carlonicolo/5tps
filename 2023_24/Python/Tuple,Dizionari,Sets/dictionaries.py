thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
print(thisdict["brand"])

for x in thisdict:
    print(x)
    
print(thisdict["colors"])

for x in thisdict["colors"]:
    print(x)