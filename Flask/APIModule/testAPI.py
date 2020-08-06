import unittest
import APIRequest
import random
from APIRequest import API_ENDPOINT_FORECAST
from APIRequest import API_ENDPOINT_CURRENT

'''
Class to test APIRequest connection
'''
class TestAPIRequest(unittest.TestCase):

    def test_weather_1(self):
        test_user_weather = APIRequest.UserWeatherRequest("Corvalis", 8,"USA", "Oregon")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

    def test_weather_2(self):
        test_user_weather = APIRequest.UserWeatherRequest("Seattle", 8,"USA", "Washington")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

    def test_weather_3(self):
        test_user_weather = APIRequest.UserWeatherRequest("Portland", 8,"USA", "Oregon")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

    def test_weather_4(self):
        test_user_weather = APIRequest.UserWeatherRequest("Los Angeles", 8,"USA", "California")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

    def test_weather_5(self):
        test_user_weather = APIRequest.UserWeatherRequest("San Diego", 8,"USA", "California")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

    def test_weather_6(self):
        test_user_weather = APIRequest.UserWeatherRequest("Irvine", 8,"USA", "California")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

    def test_weather_7(self):
        test_user_weather = APIRequest.UserWeatherRequest("New York", 8,"USA", "New York")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

    def test_weather_8(self):
        test_user_weather = APIRequest.UserWeatherRequest("Miami", 8,"USA", "Florida")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

    def test_weather_9(self):
        test_user_weather = APIRequest.UserWeatherRequest("Chicago", 8,"USA", "Illinois")
        self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)


        
        
# Run unit tests
if __name__ == '__main__':
    unittest.main()
