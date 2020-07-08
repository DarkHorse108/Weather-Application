#config contains our API keys, this config file is included in .gitignore
#requests allow us to make the GET requests to the API
import config, requests, sys

#Below is the URL of the api endpoint for Weatherbit.io
API_ENDPOINT = "https://api.weatherbit.io/v2.0/forecast/daily"

#Below is the constant that will determine the number of days to be queried for the forecast as a whole, adjust this number which will affect the query and parsing functions below. 
FORECAST_DAYS = 7

def valid_location(string_argument):
	''' valid_location() takes a single string argument, which may represent a city, state, or country. This function returns True if the string is not blank, and also contains only alphabetical characters (ignoring whitespace) i.e. "Fort Collins", "Chicago", "Hogwarts" all return True. If the string is blank or
	contains values that are not alphabetical characters, it returns False, i.e. "", "San1 Diego!", "!$@*&#^", all return False.

	string_argument: string object

	returns: boolean object'''
	
	string_length = len(string_argument)

	#If the string argument is a blank string "", its length is 0, and we can return False
	if not string_length:
		print("Empty string argument to valid_location()", file=sys.stderr)
		return False

	#Walk down each character in the string. If the character is neither a whitespace character or strictly an alphabetical character, return False immediately
	for i in range(string_length):
		if string_argument[i].isspace() or string_argument[i].isalpha():
			continue
		else:
			print("String argument contains non-alpha characters", file=sys.stderr)
			return False

	#If we've reached this point then we have determined that the string argument is not blank, and it only contains alphabetical characters. Note that this does not mean
	#That the string_argument represents a city, state, or country that actually exists. i.e. "Hogwarts" is not a real city but would return True from this function. 
	return True

def api_request(city, country, state, number_of_days = FORECAST_DAYS):
	'''api_request() takes up to 4 arguments in the following order: city name, number of days to forecast, country name, and state name. City name is required at minimum, number of days to forecast is pre-set to 7 as our application is required to display information for a 7-day forecast. If an invalid city name or a blank
	city name is supplied, api_request() will automatically return None. Country name and State name are optional, however, to ensure that you receive the most accurate information about the specific city you desire, entering those values will help, i.e. whether you want to find the weather in Paris, France or Paris, Arkansas. 
	If the city being queried is not in the United States, the state name can be omitted. This function then creates a GET request to weatherbit.io with the supplied parameters, and returns the response as a raw JSON string.

	country: 	string object
	state:		string object
	city:		string object
	number_of_days:	integer object

	returns raw JSON or None'''
	

	#The parameter city will always be required, irregardless of country, or state.
	#If we do not receive a valid city argument, we should immediately return a None
	#from the function indicating that a valid api request could not be made. 

	#If no city string is supplied OR the city string contains non-alphabetical values after removing any whitespace, return None
	if not valid_location(city):
		return None

	#Convert number_of_days to a string object so it can be used in the GET request
	number_of_days = str(number_of_days)

	#Create a new dictionary of parameters, where the key will be the string key in the query, and the value will be the string value in the query
	parameters = dict()
	parameters = {"city": city, "days": number_of_days, "units": "I", "key": str(config.API_KEY)}

	#If we received a valid country argument, include it in our dictionary of parameters. If we do not, it will not be included and the Country will be inferred by the API to the best of its ability.
	if valid_location(country):
		parameters["country"] = country		
	else:
		print("No/Invalid Country Argument")

	#If we received a valid state argument (if in the U.S.), include it in our dictionary of parameters. If we do not, it will not be included and the State will be inferred by the API to the best of its ability.
	if valid_location(state):
		parameters["state"] = state
	else:
		print("No/Invalid State Argument")

	#Send the GET request to the API with our dictionary of parameters
	response = requests.get(url = API_ENDPOINT, params = parameters)

	#Return our JSON object response from the function
	return response

def parse_api_response(response):
	'''parse_api_response() takes a JSON object response from the Weatherbit API and creates a list of 7 dictionary objects, each object representing a day in the 7 day forecast, from day 0 to day 6. Each day contains the following information:
	city name, country, date, current temperature (F), high temperature (F), low temperature (F), chance of precipitation (%), and a short description of the weather provided by the API. If the argument supplied is a None object, or is a blank string object
	indicating an error or issue in the original API request, this function returns a None object. 

	response:	raw JSON string
	returns:	list object, or None'''
	
	#If the API response we are trying to parse is a None object, or is an empty string, it means that the GET request that produced this response was invalid because the location supplied was empty or contained non-alpha characters in api_request(). Automatically return None from this function to indicate
	#that no information could be retrieved from the argument that has been given to us
	if (response == None):
		return None
	#If the response we get is a status code of 204, we entered a location that while a valid string input, is not a location that exists in the API's database
	elif response.status_code == 204:
		print("API call successful, however location queried does not exist", file=sys.stderr)
		return None
	#If the response we get is out of the 200 range, some more significant error has occured, return None
	elif response.status_code not in (200, 201, 202):
		print("API call successful, however a status error occured: {}".format(response.status_code), file=sys.stderr)
		return None
	#The response we get back is a raw string containing information about the location we are querying, convert it to a JSON object
	else:	
		response = response.json()

	#If the API response contains valid information, we take that information and store it in a list called "days", containing 7 elements i.e. days[0] through days[6] which are dictionary objects, representing the current day queried, and 6 days afterwards. 
	#For each day, i.e. day[0] which would be today, it contains the following keys:
	#"city_name"	represents the name of the city 
	#"country"		represents the country where the above city is found
	#"date"			represents the date of the day you are indexing into
	#"current_temp"	represents the current temperature in Farenheit
	#"high_temp"	represents the highest temperature forecasted for that day in Farenheit
	#"low_temp"		represents the lowest temperature forecasted for that day in Farenheit
	#"precip_chance"	represents the percentage chance of rain
	#"weather description"	represents a short general summary of the current weather conditions, i.e. "sunny with no clouds"
			
	country = response["country_code"]
	city_name = response["city_name"]
	response_days = response["data"]
		
	days = []
	for i in range(FORECAST_DAYS):
		days.append(dict())

	for number in range(FORECAST_DAYS):
		days[number]["city_name"] = city_name
		days[number]["country"] = country
		days[number]["date"] = response_days[number]["valid_date"]
		days[number]["current_temp"] = response_days[number]["temp"]
		days[number]["high_temp"] = response_days[number]["max_temp"]
		days[number]["low_temp"] = response_days[number]["low_temp"]
		days[number]["precip_chance"] = response_days[number]["pop"]
		days[number]["weather_description"] = response_days[number]["weather"]["description"]

	return days

def get_weather(city, country = "", state = ""):
	'''get_weather() takes 3 string parameters: city is the name of the city you are requesting the 7-day forecast of, this value is required. The other 2 string parameters, country and state are optional and can be left empty. 
	For greater accuracy of the results, supplying country, or country and state in the case of a U.S. city is preferrable, otherwise the API will attempt to provide information for the most relevant city, if there are multiple cities with the same name. Example calls to get_weather()
	are: get_weather("Berlin"), get_weather("Paris, France"), and get_weather("San Diego", "United States", "California"). 

	If any of the supplied arguments are invalid for any reasons, i.e. the city does not exist or it is spelled incorrectly, get_weather() will return None. Otherwise it returns a list object containing 7 dictionary objects containing forecast information for 7 days for the supplied city.
	For more details about the value list that is returned see the notes below:
		#If the API response contains valid information, we take that information and store it in a list called "days", containing 7 elements i.e. days[0] through days[6] which are dictionary objects, representing the current day queried, and 6 days afterwards. 
		#For each day, i.e. day[0] which would be today, it contains the following keys:
		#"city_name"	represents the name of the city 
		#"country"		represents the country where the above city is found
		#"date"			represents the date of the day you are indexing into
		#"current_temp"	represents the current temperature in Farenheit
		#"high_temp"	represents the highest temperature forecasted for that day in Farenheit
		#"low_temp"		represents the lowest temperature forecasted for that day in Farenheit
		#"precip_chance"	represents the percentage chance of rain
		#"weather_description"	represents a short general summary of the current weather conditions, i.e. "sunny with no clouds"

		i.e. days[0] = {"city_name": "Paris", "country": "France", "date": "2020-07-08", "current_temp": "80.1", "high_temp": "85.2", "low_temp": "76.3", "precip_chance": "30", "weather_description": "clear skies"}
			 days[1] = {"city_name": "Paris", "country": "France", "date": "2020-07-08", "current_temp": "82.1", "high_temp": "84.2", "low_temp": "78.3", "precip_chance": "0", "weather_description": "overcast clouds"}
			 days[2] = {...}
			 ...
			 days[6] = {...}

	city:	string object
	country:	string object
	state:	string object

	returns:	list object or None'''
	

	return parse_api_response(api_request(city, country, state))

if __name__ == "__main__":
	print(get_weather("Paris", "France"))