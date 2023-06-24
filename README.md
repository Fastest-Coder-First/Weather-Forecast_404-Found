# Weather Forecast Command-Line Tool  🌞🌧️
This command-line tool allows you to fetch and display weather forecast data for a specific city using the Open Weather Map API. It leverages Python to make API requests, parse the data, and provide a user-friendly output.

## Problem Statement 
Create a command-line tool that accepts a city's name and returns the weather forecast. Leverages Open Weather Map API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

## Features

- Fetches current weather data for a specified city
- Displays the main weather condition and description
- Converts temperature from Kelvin to Celsius
- Converts pressure from hPa to mmHg
- Converts visibility from meters to kilometres
- Displays additional weather data such as humidity, wind speed, clouds, sunrise, sunset, and timezone

## Credits :clap:

- Powered OpenWeatherMap API for weather data.
- AI assistance provided by GitHub Copilot for ease of code and task generation
  
## Github Copilot 
- GitHub Copilot is an AI-powered coding tool that suggests code snippets and completes code as you type. It is an extension of the Visual Studio Code editor and it can be used in various programming languages such as Python, JavaScript, TypeScript, and many more.
- The utilization of Copilot in our code significantly reduced our workload. It provided helpful suggestions in the form of code snippets. Activating Copilot is as simple as only adding a comment, and when we write a regular English sentence within that comment, Copilot intelligently converts it into a relevant code snippet and gives suggestions.
- It just needs a comment to activate it and  if we use an English sentence it will convert that to a code snippet
- Overall, GitHub Copilot is a powerful tool that can help you save time, improve your code quality, and enhance your learning and collaboration with other developers.


## Prerequisites 🛠️

- Python 3
- `requests` library (install using `pip install requests)
- import datetime
- import requests
- import argparse
- import json
- import sys

## :building_construction: Architectural Flow

The Weather CLI tool follows a simple and straightforward architectural flow. The main components involved in the flow are:

1. **User Input**: Retrieve the weather forecast for which the user enters the city name.

2. **Command-Line Interface**: The command-line interface processes user input and forwards it to the next stage.

3. **API Integration**: The API integration component retrieves weather data for the given city using the OpenWeatherMap API. It creates the API request URL using the city name and API key provided, then sends a GET request to the API endpoint.

4. **Data Parsing**: After receiving the API response, the data parsing component retrieves the pertinent weather information from the JSON response. It retrieves the primary weather conditions, full descriptions, temperature, pressure, humidity, visibility, sunrise and sunset times.

5. **Data Conversion**: During this stage, certain data conversions are performed. They include a temperature from kelvin to Celsius, pressure to mmHg, and visibility to km. 


## Run the command-line tool 🚀:
- First install all dependencies by running,
```bash
  pip install -r "requirements.py"
```
- Run the code by using,
```bash
  python main.py (city)
```
- where inplace of 'city' type the name of city whose weather details you want to see.
- Example:
``` bash
  python main.py bangalore
```
## Snapshots 📷
<img width="472" alt="image" src="https://github.com/Fastest-Coder-First/Weather-Forecast_404-Found/assets/88924201/37b68a97-a931-4991-9278-bd8876222559">




## :busts_in_silhouette: Collaborators

- [Fastest-Coder-First](https://github.com/Fastest-Coder-First)
- [Pooja Harihar](https://github.com/poojaharihar03)
- [Anish V V](https://github.com/anish2105)
- [Ishita Singhal](https://github.com/ishita-singhal)


