import unittest
import APIRequest
import random

'''
Class to test APIRequest connection
'''
class TestAPIRequest(unittest.TestCase):

    # Method to test a valid request 
    def test_valid_request_example_1(self):
        request = APIRequest.UserWeatherRequest("Fort Wayne", "USA", "Indiana")
        self.assertTrue(request.has_valid_city_name())

    # Method to a valid get weather 
    def test_get_weather_example_1(self):
        request = APIRequest.UserWeatherRequest("Fort Wayne", "USA", "Indiana")
        self.assertNotEqual(APIRequest.get_weather(request),None)

    # Method to a valid get weather 
    def test_valid_request_example_2(self):
        request = APIRequest.UserWeatherRequest("San Diego", "USA", "California")
        self.assertTrue(request.has_valid_city_name())

    # Method to a valid get weather 
    def test_get_weather_example_2(self):
        request = APIRequest.UserWeatherRequest("San Diego", "USA", "California")
        self.assertNotEqual(APIRequest.get_weather(request),None)

    # Method to test a valid get weather 
    def test_valid_request_example_3(self):
        request = APIRequest.UserWeatherRequest("Boston", "USA", "California")
        self.assertTrue(request.has_valid_city_name())

    # Method to test a valid get weather 
    def test_get_weather_example_3(self):
        request = APIRequest.UserWeatherRequest("Boston", "USA", "Massachusetts")
        self.assertNotEqual(APIRequest.get_weather(request),None)

    # Method to test a invalid request that contain special characters
    def test_valid_request_example_4(self):
        request = APIRequest.UserWeatherRequest("Tallaha$$ee", "USA", "Florida")
        self.assertFalse(request.has_valid_city_name())

    # Method to test a invalid get weather that contain special characters
    def test_get_weather_example_4(self):
        request = APIRequest.UserWeatherRequest("Tallaha$$ee", "USA", "Florida")
        self.assertEqual(APIRequest.get_weather(request),None)

    #Method to test a valid request but lack of information
    def test_valid_request_example_5(self):
        request = APIRequest.UserWeatherRequest("Denver", "Colorado")
        self.assertTrue(request.has_valid_city_name())


    # Method to test a invalid request with non-exist city
    def test_get_weather_example_5(self):
        request = APIRequest.UserWeatherRequest("aaaaaaaa", "USA", "New York")
        self.assertEqual(APIRequest.get_weather(request),None)

    


        
        
# Run unit tests
if __name__ == '__main__':
    unittest.main()
