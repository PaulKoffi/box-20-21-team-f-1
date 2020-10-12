# # rocketApiTest.py

# from services.rocket.src.run import app
import unittest
import requests


# import ast


class RocketApiTest(unittest.TestCase):
    API_URL = "http://localhost:8000"
    ROCKETS_URL = "{}/rockets".format(API_URL)
    ROCKET_URL = "{}/rocket/cotonou".format(API_URL)

    def test_1_get_all_rockets(self):
        response = requests.get(RocketApiTest.ROCKETS_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 6)
    # def test_get_all_rockets(self):
    #     tester = app.test_client()
    #     response_bytes = tester.get("/rockets")
    #     response_dict_str = response_bytes.data.decode("UTF-8")
    #     reponse_dict = ast.literal_eval(response_dict_str)
    #     self.assertEqual(len(reponse_dict), 3)

    # def test_get_rocket_by_name(self):
    #     tester = app.test_client()
    #     response_bytes = tester.get("/rocket/cotonou")
    #     response_dict_str = response_bytes.data.decode("UTF-8")
    #     reponse_dict = ast.literal_eval(response_dict_str)
    #     self.assertEqual(reponse_dict['status'], "it's risky")


if __name__ == "__main__":
    unittest.main()
