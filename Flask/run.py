#If you HAVE NOT set up your virtual environment follow lines 2-7 below. If you have, skip lines 2-7.
#In bash create your virtualenv environment to contain all the dependencies to run the Flask application
#bash
#virtualenv venv -p python3
#source./venv/bin/activate
#pip3 install --upgrade pip
#pip install -r requirements.txt

#If you HAVE set up your virtual environment, run the application non-persistently as follows
#where the XXXXX must be replaced by a random/available port number above 8000, i.e. 8912:
#source ./venv/bin/activate
#export FLASK_APP=run.py
#python -m flask run -h 0.0.0.0 -p XXXX --reload


#The line below looks in the folder called Weather App, and executes the WeatherApp.py file.
#Specifically, we import the object labeled WeatherApp that was instantiated in line 6 of the WeatherApp.py script.
from WeatherApp.WeatherApp import WeatherApp
#for example, the above line tells to run WeatherApp.py in WeatherApp/ 


