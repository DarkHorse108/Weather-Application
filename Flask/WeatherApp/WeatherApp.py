# Import Flask and the module required to render HTML pages and deal with
# requests and redirection between pages
from flask import Flask, render_template, request, redirect
import requests, APIRequest

# Instantiate the Flask Application/Object
WeatherApp = Flask(__name__)

# temp API key
API_KEY = '5bf5950b4a834db092b5870ac750a47f'


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
            if forecast_days != None:

                # process data here
                return render_template('results.html', forecast_days=forecast_days)

                print(forecast_days[0])

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

            # If so, attempt to send the information to tthe API and retrieve the parsed information from the response.
            # If successful, forecast_days should be a list of dictionary objects.
            forecast_days = APIRequest.get_weather(test_user_weather_request)

            # If forecast_days is NOT None, we received a valid/usable information from the API
            if forecast_days != None:
                # process data here
                return render_template('results.html', forecast_days=forecast_days)

                print(forecast_days[0])

        # If the city name was not valid, or if the API response indicates that weather information could not be
        # retrieved using the location information we supplied it, return the user to the home page to start again
        return redirect('/')

# test route
@WeatherApp.route('/test_template', methods=['GET', 'POST'])
def test_route():
    if request.method == 'GET':
        return render_template('test_template.html', city_name='PLACEHOLDER')

    elif request.method == 'POST':
        input_location_name = request.form['location-name']

        request_url = 'https://api.weatherbit.io/v2.0/forecast/daily?city=' + input_location_name + '&key=' + API_KEY
        response = requests.get(request_url)
        weather_data = response.json()

        return render_template('test_template.html', city_name=weather_data['city_name'])


# To start flask locally
# if __name__ == '__main__':
#     WeatherApp.run(debug=True)
