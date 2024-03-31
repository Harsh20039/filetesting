import unittest
import requests

class TestWebsiteLoading(unittest.TestCase):

    def test_website_loading(self):
        url = 'https://atg.world'
        print("Connecting to {}...".format(url))
        try:
            response = requests.get(url)
            self.assertEqual(response.status_code, 200)
            print("Website loaded successfully!")
        except requests.ConnectionError:
            print("Failed to connect to the website!")
            self.fail("Failed to connect to the website")

if __name__ == '__main__':
    unittest.main()
