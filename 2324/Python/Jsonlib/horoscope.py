import requests
import json

# pip install requests

# Make the GET request to the horoscope API
response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=virgo&day=today")
data = response.json()  # Convert the response to JSON

print("Data -> ", data)
print("\n")

# Store the JSON data in a file
with open("horoscope_data.json", "w") as file:
    json.dump(data, file)

print("Data stored successfully!")

print(" ")

# Retrieve JSON data from the file
with open("horoscope_data.json", "r") as file:
    data = json.load(file)

# Access and process the retrieved JSON data
date = data["data"]["date"]
horoscope_data = data["data"]["horoscope_data"]

# Print the retrieved data
print(f"Horoscope for date {date}: {horoscope_data}")
