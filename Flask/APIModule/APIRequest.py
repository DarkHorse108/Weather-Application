'''todo:
    check if the data we're displaying as current weather is actually current
    the current time is the server's time. we should display the local
        time (labeled as local time in the html) *DONE*
'''

# config contains our API keys, this config file is included in .gitignore
# requests allow us to make the GET requests to the API
import requests, sys, datetime, calendar
import pytz
import config

# from APIModule import config
#from APIModule import config

# Below is the URL of the api endpoint for Weatherbit.io
API_ENDPOINT_FORECAST = "https://api.weatherbit.io/v2.0/forecast/daily"
API_ENDPOINT_CURRENT = " https://api.weatherbit.io/v2.0/current"
#API_ENDPOINT2 = "https://api.weatherbit.io/v2.0/forecast/energy"

# Below is the constant that will determine the number of days to be queried for the forecast as a whole, adjust this
# number which will affect the query and parsing functions below.
FORECAST_DAYS = 8
CURRENT_DAY = 1

class UserWeatherRequest:
    def __init__(self, city, number_of_days, country="", state=""):
        self.city = city
        self.number_of_days = number_of_days
        self.country = country
        self.state = state
        

    def generate_formatted_request_parameters(self):
        # There must be a city to make get weather data. country and state are optional.
        # If we do not receive a valid city argument, we should immediately return a None
        # from the function indicating that a valid api request could not be made.

        # If no city string is supplied OR the city string contains non-alphabetical values after removing any
        # whitespace, return None
        if not self.has_valid_city_name():
            print("No/Invalid City name")
            return None

        if self.number_of_days == CURRENT_DAY:

             parameters = {"city": self.city, "units": "I", "key": str(config.API_KEY)}

        elif self.number_of_days == FORECAST_DAYS:
            
            # Create a new dictionary of parameters, where the key will be the string key in the query, and the value will
            # be the string value in the query
            parameters = {"city": self.city, "days": str(self.number_of_days), "units": "I", "key": str(config.API_KEY)}

        # If we received a valid country argument, include it in our dictionary of parameters. If we do not, it will
        # not be included and the Country will be inferred by the API to the best of its ability.
        if is_valid_location_string(self.country):
            parameters["country"] = self.country
        else:
            print("No/Invalid Country name")

        # If we received a valid state argument (if in the U.S.), include it in our dictionary of parameters.
        # If we do not, it will not be included and the State will be inferred by the API to the best of its ability.
        if is_valid_location_string(self.state):
            parameters["state"] = self.state
        else:
            print("No/Invalid State name")

        return parameters

    def has_valid_city_name(self):
        if is_valid_location_string(self.city):
            return True
        return False

def get_api_response(parameters):
    # Send the GET request to the API with our dictionary of parameters
    # Return our JSON object response from the function
    return requests.get(url=API_ENDPOINT, params=parameters)


def api_response_to_json(response):
    '''api_response_to_json() takes a Requests response, checks if it's valid, then converts it to json and returns it

    response:   Requests response
    returns:    JSON object'''

    # The response we get back is a raw string containing information about the location we are querying, convert it to
    # a JSON object
    return response.json()


def get_weather_json(user_weather_request, endpoint_url):
    formatted_request_parameters = user_weather_request.generate_formatted_request_parameters()
    if formatted_request_parameters:
        api_response = requests.get(url=endpoint_url, params=formatted_request_parameters)
        if is_valid_response(api_response):
            return api_response.json()
        else:
            print("Invalid api response")
    return None


def get_day_of_week(date_string):
    '''Takes a string in the format YYYY-MM-DD and converts it into a string representing which day of the week it
     is, i.e. "Monday", "Tuesday", "Wednesday" and returns that string.'''

    day_of_the_week = datetime.datetime.strptime(date_string, '%Y-%m-%d').weekday()

    return str(calendar.day_name[day_of_the_week])


def get_month_name(date_string):
    '''Takes a string in the format YYYY-MM-DD and converts it into a string representing which month of the year it
    is, i.e. "January", "February", and returns that string'''
    month = datetime.datetime.strptime(date_string, '%Y-%m-%d').strftime('%B')

    return str(month)


def get_current_calendar_day_number():
    return datetime.datetime.today().day


def get_current_hour():
    return str(datetime.datetime.now().strftime('%I'))


def get_current_minute():
    return str(datetime.datetime.now().strftime('%M'))


def get_current_am_pm():
    return str(datetime.datetime.now().strftime('%p'))


def create_current_12_hour_time():
    return get_current_hour() + ':' + get_current_minute() + ' ' + get_current_am_pm()


def generate_formatted_per_day_weather_data(forecast_response_json, current_response_json):
    '''generate_formatted_per_day_weather_data() takes a Weatherbit API response  JSON object  and creates a list of dictionary
    objects, each object representing a day in the 7 day forecast, from day 0 to day 6. Each day contains the following
    information: city name, country, date, current temperature (F), high temperature (F), low temperature (F), chance of
    precipitation (%), and a short description of the weather provided by the API. If the argument supplied is a None
    object, or is a blank string object indicating an error or issue in the original API request, this function returns
    a None object.

    response:   raw JSON string
    returns:    list object, or None'''

    # If the API response contains valid information, we take that information and store it in a list called "days",
    # containing 7 elements i.e. days[0] through days[6] which are dictionary objects, representing the current day
    # queried, and 6 days afterwards.

    # For each day, i.e. day[0] which would be today, it contains the following keys:
    # "date"            represents the date of the day you are indexing into
    # "current_temp"    represents the current temperature in Farenheit
    # "high_temp"   represents the highest temperature forecasted for that day in Farenheit
    # "low_temp"        represents the lowest temperature forecasted for that day in Farenheit
    # "precip_chance"   represents the percentage chance of rain
    # "weather description" represents a short general summary of the current weather conditions, i.e. "sunny with no clouds"

    per_day_weather_json = forecast_response_json["data"]

    timezone = forecast_response_json["timezone"]

    days = generate_list_of_dicts(FORECAST_DAYS)

    for i in range(FORECAST_DAYS):
        days[i]["date"] = per_day_weather_json[i]["valid_date"]
        #days[i]["calendar_day"] = get_current_calendar_day_number() // This uses the calendar day of the machine the program is running on!!! do not use - John Sy
        days[i]["calendar_day"] = int(per_day_weather_json[i]["valid_date"][-2::])
        days[i]["day"] = get_day_of_week(days[i]["date"])
        days[i]["month"] = get_month_name(days[i]["date"])
        days[i]["current_temp"] = round(per_day_weather_json[i]["temp"])
        days[i]["high_temp"] = round(per_day_weather_json[i]["max_temp"])
        days[i]["low_temp"] = round(per_day_weather_json[i]["low_temp"])
        days[i]["precip_chance"] = per_day_weather_json[i]["pop"]  # UPDATE: It works, some locations do in fact have a 0% precip chance while others have more expected values like 20-50%. This value is fine/working/
        days[i]["weather_description"] = per_day_weather_json[i]["weather"]["description"]
        days[i]["weather_icon"] = per_day_weather_json[i]["weather"]["icon"]
        days[i]["weather_code"] = per_day_weather_json[i]["weather"]["code"]
        days[i]["humidity"] = per_day_weather_json[i]["rh"]
        days[i]["wind_speed"] = per_day_weather_json[i]["wind_spd"]

    days[0]["current_temp"] = int(current_response_json["data"][0]["temp"])
    days[0]["precip_chance"] = current_response_json["data"][0]["precip"]
    days[0]["weather_description"] = current_response_json["data"][0]["weather"]["description"]
    days[0]["weather_icon"] = current_response_json["data"][0]["weather"]["icon"]
    days[0]["weather_code"] =  current_response_json["data"][0]["weather"]["code"]

    days.append(timezone)
    days.append(get_timezone_time(timezone))

    return days


def get_api_returned_location_info(response_json):
    # "city_name"   represents the name of the city
    # "country"     represents the country where the above city is found
    # "state"       represents the state code where the above city is found

    # If the city being queried is an international location, the API returns the state code as an integer,
    # which should fail the is_valid_location_string() function. We will set the state_code as an empty
    # string so that when the state_code is populated in the results page, nothing appears for the state
    # for cities outside of the U.S.

    # 3 = city_name, state_code, and country
    location = dict()

    location["city_name"] = response_json["city_name"]
    if is_valid_location_string(response_json["state_code"]):
        location["state_code"] = response_json["state_code"]
    else:
        state_code = ""
    location["country"] = response_json["country_code"]

    return location


''' helpers '''


def generate_list_of_dicts(list_len):
    list_of_dicts = []
    for _ in range(list_len):
        list_of_dicts.append(dict())
    return list_of_dicts


def is_valid_location_string(location_name_string):
    ''' is_valid_location_string() takes a single string argument, which may represent a city, state, or country. This
    function returns True if the string is not blank, and also contains only alphabetical characters
    (ignoring whitespace) i.e. "Fort Collins", "Chicago", "Hogwarts" all return True. If the string is blank or
    contains values that are not alphabetical characters, it returns False, i.e. "", "San1 Diego!", "!$@*&#^",
    all return False.

    string_argument: string object

    returns: boolean object'''

    # If the string argument is a blank string "" we can return False
    if not location_name_string:
        print("Empty string argument to is_valid_location_string()", file=sys.stderr)
        return False

    if contains_only_spaces_and_alphas(location_name_string):
        return True
    else:
        print("String argument contains non-alpha characters", file=sys.stderr)


def contains_only_spaces_and_alphas(location_name_string):
    # Walk down each character in the string. If the character is neither a whitespace character or strictly an
    # alphabetical character, return False immediately
    for char in location_name_string:
        if not is_character_space_or_alpha(char):
            return False
    return True


def is_character_space_or_alpha(char):
    if char.isspace() or char.isalpha():
        return True
    else:
        return False


def is_valid_response(response):
    # If the API response we are trying to parse is a None object, or is an empty string, it means that the GET request
    # that produced this response was invalid because the location supplied was empty or contained non-alpha characters
    # in api_request(). Automatically return None from this function to indicate
    # that no information could be retrieved from the argument that has been given to us
    if response is None:
        return False
    # If the response we get is a status code of 204, we entered a location that while a valid string input, is not a
    # location that exists in the API's database
    elif response.status_code == 204:
        print("API call successful, however location queried does not exist", file=sys.stderr)
        return False
    # If the response we get is out of the 200 range, some more significant error has occured, return None
    elif response.status_code not in (200, 201, 202):
        print("API call successful, however a status error occured: {}".format(response.status_code), file=sys.stderr)
        return False

    return True


def get_timezone_time(loc_timezone):
    """
    Grabs a parameter of a timezone (eg: 'America/Indiana/Indianapolis') and converts it to local time with AM/PM.

    :returns timezone
    """
    current_time = datetime.datetime.now(pytz.timezone(loc_timezone))
    
    current_time = current_time.strftime('%I:%M %p')

    #Modify string to not include the extraneous 0 in front of the hours i.e. 06:00 AM, however if the time is 10:00AM it will be displayed correctly as such/
    hours = current_time[:2]
    hours = int(hours)
    current_time = current_time[2::]

    return str(hours) + current_time

if __name__ == "__main__":
    test_user_weather_request = UserWeatherRequest("Fort Wayne", 8,"USA", "Indiana")

    if test_user_weather_request.has_valid_city_name():
        print(generate_formatted_per_day_weather_data(get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST),get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)))
