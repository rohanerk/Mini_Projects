# Fetching Current Weather Data

# The program does the following:

# 1. Reads the requested location from the command line
# 2. Downloads JSON weather data from OpenWeatherMap.org
# 3. Converts the string of JSON data to a python data structure
# 4. Prints the weather for today and the next two days

# a. Join strings in sys.argv to get the location
# b. calls requests.get() to download the weather data
# c. Call json.loads() to convert the JSON data to python data structure
# d. Print the weather forecast

#! python3
# quickWeather.py - Prints the weather for a location from command line

import requests, json, sys

# Compute the location from command line argumens

if len(sys.argv)<2:
    print('Usage: quickWeather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:]) # sys.argv will have atleast 1 element (sys.argv[0]) which contains the python script's filename

# Download the JSON data from OpenweatherMap.org API

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status() # if no error is raised, the downloaded text will be in response.text

# Load JSON Data and Print weather

weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
