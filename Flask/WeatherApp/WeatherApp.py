#Import Flask and the module required to render HTML pages and deal with
#requests and redirections between pages
from flask import Flask, render_template, request, redirect

#Instantiate the Flask Application/Object
WeatherApp = Flask(__name__)

#The code below handles the default URL/Landing page i.e. flipN.oregonstate.edu:PORTNUMBER automatically executes the view/function below
@WeatherApp.route('/')
def index():

	#We render the file home.html contained in the templates folder
	return render_template('home.html')
    

