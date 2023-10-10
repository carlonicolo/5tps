import json

def main():

    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York", "cars": [{"model": "BMW 230", "mpg": 27.5},{"model": "Ford Edge", "mpg": 24.1}]}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["age"])

    print(y["name"])

    print(type(y))
    
    print(y["cars"])
    
    print(type(y["cars"]))
    
    print(type(y["cars"][0]))
    
    print(y["cars"][0]["model"])
    
if __name__ == "__main__":
    main()
    