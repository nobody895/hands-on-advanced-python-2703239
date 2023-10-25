# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snowdays = list(filter(lambda x: x['snow'] > 0.0, weatherdata))
# print(len(weatherdata))
# print(len(snowdays))

# TODO: pretty-print the resulting data set
# pprint.pp(snowdays)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(d):
    summer_months = ["-07-", "-08-"]
    for sm in summer_months:
        if sm in d['date'] and d['prcp'] >= 1:
            return True
    return False

summer_rain_days = list(filter(is_summer_rain_day, weatherdata))
pprint.pp(summer_rain_days)