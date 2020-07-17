# CS361-Slackers-WeatherApp
CS361 W2020 Team Slackers Python Weather Web Application

To run this web application, please follow the instructions below. Note that these instructions are for a linux environment and reflect running the application in OSU ENGR's flip servers.

1. Create a new folder to hold the repository files, i.e. mkdir WeatherApplication

2. In your new folder, enter the following command:

git clone https://github.com/DarkHorse108/CS361-Slackers-WeatherApp

3. Sign up for a Weatherbit.io API key at: https://www.weatherbit.io/

4. Open the file /Flask/APIModule/config.py in your text editor/IDE and replace the value of the variable API_KEY with your API key as a string value on the righthand side.

5. Return to the folder /Flask

6. Execute the shell script RunWeatherApp.sh OR run the following commands in your command line to set up your virtual environment with all of the required modules:

bash
virtualenv venv -p python3
source ./venv/bin/activate
pip3 install --upgrade pip
pip install -r requirements.txt

7. Then, enter the following commands in your command line:

source ./venv/bin/activate
export FLASK_APP=run.py

8. Run the following command in your command line, replacing YOUR_PORT_NUMBER with a valid random 4 digit port number that is available for this process to run on, i.e. 8666, 8667, etc.:

python -m flask run -h 0.0.0.0 -p YOUR_PORT_NUMBER --reload

9. The application should now be running and viewable using your browser on your local host at the portnumber you specified. If you are using one of the OSU ENGR flip servers, *you will need to be connected to the OSU VPN*, and then the address your application is on would be:

http://flipN.engr.oregonstate.edu:YOUR_PORT_NUMBER

where flipN is which flip server (1, 2, 3) you are running the application on. i.e. http://flip3.engr.oregonstate.edu:YOUR_PORT_NUMBER
