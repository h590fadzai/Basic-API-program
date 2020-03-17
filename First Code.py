from urllib.request import urlopen
import json

# Init Variables
welcomeMessage = "/// Aloha, welcome to paradise \\\\"

# Welcome to the Weather API
print(welcomeMessage)
print("")

# Get WOEID
link = "https://type.fit/api/quotes"
response = urlopen(link)
data = json.loads(response.read())

# Print it to the screen
print(data[7]["text"])
print(data[7]["author"])
