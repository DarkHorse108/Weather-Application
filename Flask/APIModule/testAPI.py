import unittest
import APIRequest
import random
from APIRequest import API_ENDPOINT_FORECAST
from APIRequest import API_ENDPOINT_CURRENT
import json
import random


'''
Class to test APIRequest connection
'''


#Sources: https://gist.github.com/ahmu83/38865147cf3727d221941a2ef8c22a77

class TestAPIRequest(unittest.TestCase):

    def test_weather(self):
        #Use random test to test all USA cities
        f = open("data.json")
        data = json.load(f)
        f.close()
        states = list(data.keys())

        for i in range(50):
            state_index = random.randint(0,50)
            cities = list(data[states[state_index]])
            test_state = states[state_index]
            city_index = random.randint(0,(len(cities)-1))
            test_city = cities[city_index]
            print("PASSED", test_city, ",",test_state)
            test_user_weather = APIRequest.UserWeatherRequest(test_city, 8,"USA", test_state)
            self.assertNotEqual(APIRequest.get_weather(test_user_weather),None)

        
        
# Run unit tests
if __name__ == '__main__':
    unittest.main()
