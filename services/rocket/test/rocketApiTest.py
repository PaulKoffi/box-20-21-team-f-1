# # rocketApiTest.py

import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'src')))

from run import app
import unittest
import ast

class RocketApiTest(unittest.TestCase):
    
    def test_get_all_rockets(self):
        tester = app.test_client()
        response_bytes = tester.get("/rockets")
        response_dict_str = response_bytes.data.decode("UTF-8")
        reponse_dict = ast.literal_eval(response_dict_str)
        self.assertEqual(len(reponse_dict),3)

    def test_get_rocket_by_name(self):
        tester = app.test_client()
        response_bytes = tester.get("/rocket/cotonou")
        response_dict_str = response_bytes.data.decode("UTF-8")
        reponse_dict = ast.literal_eval(response_dict_str)
        self.assertEqual(reponse_dict['status'],"it's risky")

if __name__ == "__main__":
    unittest.main()