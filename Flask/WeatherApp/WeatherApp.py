# Import Flask and the module required to render HTML pages and deal with
# requests and redirection between pages
from flask import Flask, render_template, request, redirect
from APIModule import APIRequest
from WeatherWarningsModule import WeatherWarnings
from WeatherMapModule import WeatherMap
import requests
import datetime

# Instantiate the Flask Application/Object
WeatherApp = Flask(__name__)

# controls the spacing in degrees between the weather grid points
WEATHER_GRID_SPACING = 0.5

# The code below handles the default URL/Landing page i.e. flipN.oregonstate.edu:PORTNUMBER automatically executes
# the view/function below
@WeatherApp.route('/', methods=['GET', 'POST'])
def index():
    
     return render_template('home.html')
  
@WeatherApp.route('/results', methods=['GET', 'POST'])
def results():
    # If the user arrives at this page for the first time, they will be shown home.html
    if request.method == 'GET':

        return render_template('home.html')

    # If they are arriving at this page via POST, they have used one or more of the input forms. We collect that data
    # here
    elif request.method == 'POST':

        # Collect string input from the cityInput, countryInput, and stateInput forms
        user_city_input = request.form['cityInput']
        user_country_input = request.form['countryInput']
        user_state_input = request.form['stateInput']

        # Instantiate a UserWeatherRequest object called test_user_weather_request
        user_weather_request_current = APIRequest.UserWeatherRequest(user_city_input, APIRequest.CURRENT_DAY, user_country_input, user_state_input)
        user_weather_request_forecast = APIRequest.UserWeatherRequest(user_city_input, APIRequest.FORECAST_DAYS, user_country_input, user_state_input)
        # Check if the user input includes a valid city name
        if user_weather_request_forecast.has_valid_city_name():

            # If so, attempt to send the information to the API and retrieve the parsed information from the response.
            # If successful, forecast_days should be a list of dictionary objects.

            forecast_weather_json = APIRequest.get_weather_json(user_weather_request_forecast, APIRequest.API_ENDPOINT_FORECAST)
            current_weather_json = APIRequest.get_weather_json(user_weather_request_current, APIRequest.API_ENDPOINT_CURRENT)

            if forecast_weather_json and current_weather_json:
                # the api requets
                forecast_days = APIRequest.generate_formatted_per_day_weather_data(forecast_weather_json, current_weather_json)
                location = APIRequest.get_api_returned_location_info(forecast_weather_json)

                # If forecast_days is NOT None, we received a valid/usable information from the API
                if forecast_days is not None:
                    # process data here
                    # todo: eventually update time to be local time

                    # todo: delete this warning alerts test
                    # warnings = [
                    #     {'type': 'rain',
                    #      'bootstrap_alert_class': 'alert alert-warning alert-dismissible',
                    #      'days_till': 4,
                    #      'duration_days': 8},
                    #     {'bootstrap_alert_class': 'alert alert-danger alert-dismissible',
                    #      'type': 'sand',
                    #      'days_till': 7,
                    #      'duration_days': 14}
                    # ]

                    # todo: 1:8 since we ignore the first day and someone added location and time to this dict
                    # todo: need to get location and time out of this dict
                    warnings = WeatherWarnings.find_storms(forecast_days[1:8])

                    # get weather map data
                    city_coordinates = APIRequest.get_city_coordinates(forecast_weather_json)
                    weather_grid_coordinates = WeatherMap.generate_nine_point_grid(city_coordinates, WEATHER_GRID_SPACING)
                    nine_point_current_weather = []
                    for coordinate in weather_grid_coordinates:
                        coordinate_request = APIRequest.CoordinateWeatherRequest(coordinate, 1)

                        coordinate_weather_json = APIRequest.get_weather_json(coordinate_request, APIRequest.API_ENDPOINT_CURRENT)
                        coordinate_weather = APIRequest.generate_current_weather_data(coordinate_weather_json)
                        nine_point_current_weather.append(coordinate_weather)

                    print(nine_point_current_weather)

                    return render_template('results.html',
                                           forecast_days=forecast_days,
                                           location=location,
                                           warnings=warnings,
                                           nine_point_current_weather=nine_point_current_weather
                                           )

        # If the city name was not valid, or if the API response indicates that weather information could not be
        # retrieved using the location information we supplied it, return the user to the home page to start again
        return redirect('/')

# To start flask locally
if __name__ == '__main__':
    WeatherApp.run(debug=True)

# todo: replace the time functions to use local time
def get_server_hour():
    return str(datetime.datetime.now().strftime('%I'))


def get_server_minute():
    return str(datetime.datetime.now().strftime('%M'))


def get_server_minute_am_pm():
    return str(datetime.datetime.now().strftime('%p'))


def create_server_12_hour_time():
    return get_server_hour() + ':' + get_server_minute() + ' ' + get_server_minute_am_pm()
