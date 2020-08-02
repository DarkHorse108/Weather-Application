import unittest
import APIRequest
import random
from APIRequest import API_ENDPOINT_FORECAST
from APIRequest import API_ENDPOINT_CURRENT

'''
Class to test APIRequest connection
'''
class TestAPIRequest(unittest.TestCase):

    def test_valid_request_example_1(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("Corvalis", 8,"USA", "Oregon")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)

    def test_valid_request_example_2(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("Seattle", 8,"USA", "Washington")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)

    def test_valid_request_example_2(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("Portland", 8,"USA", "Oregon")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)

    def test_valid_request_example_4(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("Los Angeles", 8,"USA", "California")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)

    def test_valid_request_example_5(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("San Diego", 8,"USA", "California")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)

    def test_valid_request_example_6(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("Irvine", 8,"USA", "California")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)

    def test_valid_request_example_7(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("New York", 8,"USA", "New York")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)

    def test_valid_request_example_8(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("Miami", 8,"USA", "Florida")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)

    def test_valid_request_example_9(self):
        test_user_weather_request = APIRequest.UserWeatherRequest("Chicago", 8,"USA", "Illinois")
        forcast = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_FORECAST)
        current = APIRequest.get_weather_json(test_user_weather_request,API_ENDPOINT_CURRENT)
        data = APIRequest.generate_formatted_per_day_weather_data(forcast,current)
        self.assertNotEqual(data,None)
    

    


        
        
# Run unit tests
if __name__ == '__main__':
    unittest.main()
