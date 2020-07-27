# Import Flask and the module required to render HTML pages and deal with
# requests and redirection between pages
from flask import Flask, render_template, request, redirect
from APIModule import APIRequest
import requests
import datetime

# Instantiate the Flask Application/Object
WeatherApp = Flask(__name__)


# The code below handles the default URL/Landing page i.e. flipN.oregonstate.edu:PORTNUMBER automatically executes
# the view/function below
@WeatherApp.route('/', methods=['GET', 'POST'])
def index():
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
        test_user_weather_request = APIRequest.UserWeatherRequest(user_city_input, user_country_input, user_state_input)

        # Check if the user input includes a valid city name
        if test_user_weather_request.has_valid_city_name():

            # If so, attempt to send the information to tthe API and retrieve the parsed information from the response.
            # If successful, forecast_days should be a list of dictionary objects.
            forecast_days = APIRequest.get_weather(test_user_weather_request)

            # If forecast_days is NOT None, we received a valid/usable information from the API
            if forecast_days is not None:
                # process data here
                return render_template('results.html', forecast_days=forecast_days)

        # If the city name was not valid, or if the API response indicates that weather information could not be
        # retrieved using the location information we supplied it, return the user to the home page to start again
        return redirect('/')


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
        test_user_weather_request = APIRequest.UserWeatherRequest(user_city_input, user_country_input, user_state_input)

        # Check if the user input includes a valid city name
        if test_user_weather_request.has_valid_city_name():

            # If so, attempt to send the information to the API and retrieve the parsed information from the response.
            # If successful, forecast_days should be a list of dictionary objects.
            weather_json = APIRequest.get_weather_json(test_user_weather_request, APIRequest.API_ENDPOINT)
            if weather_json:
                # the api requets
                forecast_days = APIRequest.generate_formatted_per_day_weather_data(weather_json)
                location = APIRequest.get_api_returned_location_info(weather_json)

                # If forecast_days is NOT None, we received a valid/usable information from the API
                if forecast_days is not None:
                    print(forecast_days)
                    # process data here
                    # todo: eventually update time to be local time
                    return render_template('results.html',
                                           forecast_days=forecast_days,
                                           location=location,
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
