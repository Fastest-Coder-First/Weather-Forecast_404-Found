#Create a command-line tool that accepts a city's forecast. Leverages Open Weather Map API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.
# Importing the requests library
import datetime
import requests
import argparse
import json
import sys
import pytz
#function to get weather data for a city
def get_weather(city):
    api_key = "f5666dfdd395817a68a86cd862e98961"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    #sunrise sunset url
    sunrise_sunset_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#function that ocnverts kelvin to celsius
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
#Add a function to convert the pressure from hPa to mmHg or inHg.   
    def pressure_conversion(pressure):
        return pressure * 0.750062
#Add a function to convert the visibility from meters to km or miles.
# 1 meter = 0.001 km
# 1 meter = 0.000621371192 miles
# 1 km = 0.621371192 miles
# 1 km = 1000 meters

    def visibility_conversion(visibility):
        return visibility * 0.001        

    #try to get data from the api
    try:
        response=requests.get(url)
        response.raise_for_status()
        data=response.json()

        #parse the weather data
        main_weather=data["weather"][0]["main"]
        description=data["weather"][0]["description"]
        #round the temperature to 2 decimal places
        temp=round(kelvin_to_celsius(data["main"]["temp"]),2)
        feels_like=round(kelvin_to_celsius(data["main"]["feels_like"]),2)
        temp_min=round(kelvin_to_celsius(data["main"]["temp_min"]),2)
        temp_max=round(kelvin_to_celsius(data["main"]["temp_max"]),2)
        pressure=pressure_conversion(data["main"]["pressure"])
        humidity=data["main"]["humidity"]
        visibility=visibility_conversion(data["visibility"])
        wind_speed=data["wind"]["speed"]
        wind_deg=data["wind"]["deg"]
        clouds=data["clouds"]["all"]
        country=data["sys"]["country"]
        timezone_offset = data["timezone"]
        sunrise = datetime.datetime.utcfromtimestamp(data["sys"]["sunrise"] + timezone_offset).strftime("%H:%M:%S")
        sunset = datetime.datetime.utcfromtimestamp(data["sys"]["sunset"] + timezone_offset).strftime("%H:%M:%S")
        name=data["name"]

        #fetch sunrise and sunset data
        sunrise_sunset_response=requests.get(sunrise_sunset_url)
        sunrise_sunset_response.raise_for_status()
        sunrise_sunset_data=sunrise_sunset_response.json()
        sunrise_sunset_timezone_offset = sunrise_sunset_data["timezone"]
        sunrise_sunset_sunrise = datetime.datetime.utcfromtimestamp(sunrise_sunset_data["sys"]["sunrise"] + sunrise_sunset_timezone_offset).strftime("%H:%M:%S")
        sunrise_sunset_sunset = datetime.datetime.utcfromtimestamp(sunrise_sunset_data["sys"]["sunset"] + sunrise_sunset_timezone_offset).strftime("%H:%M:%S")
        

        #printing the weather data
        print(f"Weather forecast for {city}, {country}:")
        print(f"Main weather: {main_weather}")
        print(f"Description: {description}")
        print(f"Temperature: {temp} C" )
        print(f"Feels like: {feels_like} C")
        print(f"Minimum temperature: {temp_min} C")
        print(f"Maximum temperature: {temp_max} C")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Visibility: {visibility}")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
        sys.exit(0)
    #except the requests exception
    except requests.exceptions.RequestException as err:
        print(err)
        sys.exit(1)
    #except the json exception
    except json.decoder.JSONDecodeError as err:
        print(err)
        sys.exit(1)
    #except the key error
    except KeyError as err:
        print(err)
        sys.exit(1)
   
#main function
def main():
    parser = argparse.ArgumentParser(description="Get the weather forecast for a city.")
    parser.add_argument("city", type=str, help="Name of the city")
    
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    get_weather(args.city)
if __name__ == "__main__":
    main()
