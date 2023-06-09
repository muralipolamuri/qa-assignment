import unittest
import requests
import re
from datetime import datetime

date = ["1990-03-23", "19-09-1990"]


class NextBirthdayTest(unittest.TestCase):
    base_url = "https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday"

    def date_check(self):
        valid_length = True if (re.findall(r"[\d]{4}-[1|0][\d]-[1|2|3][\d]", self.dob)) else False
        if valid_length:
            a, b, c = str(self.dob).split('-')
            try:
                datetime(int(a), int(b), int(c))
                return True
            except ValueError:
                return False
        return False

    def test_hours_left(self):
        # Test case for unit = hour
        url = self.base_url + "?dateofbirth=" + date[0] + "&unit=hour"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200 (success)
        self.assertIn("hours left", response.json()["message"])  # Check if the response message contains "hours left"
        print("hours left", response.json()['message'])
        print(response.status_code)

    def test_days_left(self):
        # Test case for unit = day
        url = self.base_url + "?dateofbirth=" + date[0] + "&unit=day"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200 (success)
        self.assertIn("days left", response.json()["message"])  # Check if the response message contains "days left"
        print("days left", response.json()['message'])
        print(response.status_code)

    def test_weeks_left(self):
        # Test case for unit = week
        url = self.base_url + "?dateofbirth=" + date[0] + "&unit=week"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200 (success)
        self.assertIn("weeks left", response.json()["message"])  # Check if the response message contains "weeks left"
        print("weeks left", response.json()['message'])
        print(response.status_code)

    def test_months_left(self):
        # Test case for unit = month
        url = self.base_url + "?dateofbirth="+date[0]+"&unit=month"
        response = requests.get(url)
        #print(url)
        json_response = response.json()
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200 (success)
        # self.assertIn(json_response['message'] == "months left", "error")  # Check if the response message contains "months left"
        print("months left", response.json()['message'], )
        print(response.status_code)

    def test_missing_dateofbirth(self):
        # Test case for missing dateofbirth parameter
        url = self.base_url + "?unit=day"
        response = requests.get(url)
        # print(url)
        self.assertEqual(response.status_code, 400)  # Check if the response status code is 400 (bad request)
        # message contains the expected error message
        print(response.json()['message'], response.status_code)

    def test_invalid_dateofbirth(self):
        # Test case for invalid dateofbirth parameter
        url = self.base_url + "?dateofbirth="+date[1]+"&unit=day"
        #print(url)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['message'] == "Please specify dateofbirth in ISO format YYYY-MM-DD")
        # Check if the response status code is 400 (bad request)
        #print(response.json()["message"])
        print(response.content, response.status_code)

    def test_missing_unit(self):
        # Test case for missing unit parameter
        url = self.base_url + "?dateofbirth="+date[0]+"&unit="
        response = requests.get(url)
        self.assertEqual(response.status_code, 400)  # Check if the response status code is 400 (bad request)
        print(response.json()['message'])
        print(response.status_code)


if __name__ == '__main__':
    unittest.main()
