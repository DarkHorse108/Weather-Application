#Import Flask and the module required to render HTML pages and deal with
#requests and redirections between pages
from flask import Flask, render_template, request, redirect
import requests

#Instantiate the Flask Application/Object
WeatherApp = Flask(__name__)

# temp API key
API_KEY = '5bf5950b4a834db092b5870ac750a47f'

#The code below handles the default URL/Landing page i.e. flipN.oregonstate.edu:PORTNUMBER automatically executes the view/function below
@WeatherApp.route('/')
def index():

	#We render the file home.html contained in the templates folder
	return render_template('home.html')

# test route
@WeatherApp.route('/test_template', methods=['GET', 'POST'])
def test_route():
    if request.method == 'GET':
        return render_template('test_template.html', city_name = 'PLACEHOLDER')

    elif request.method == 'POST':
        input_location_name = request.form['location-name']

        request_url = 'https://api.weatherbit.io/v2.0/forecast/daily?city=' + input_location_name + '&key=' + API_KEY
        response = requests.get(request_url)
        weather_data = response.json()

        return render_template('test_template.html', city_name = weather_data['city_name'])
