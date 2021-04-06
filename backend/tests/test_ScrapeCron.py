from src.ScrapeCron import *

from unittest.mock import patch
from unittest import TestCase
import os

class UserIntefaceTest(TestCase):

    def test_scrape_webadvisor(self):
        filename, _ = scrape_to_HTML()
       
        data_dir = os.getcwd()
        today = date.today().strftime("%m-%d-%y")
        check_file = data_dir + "/data/" + "Webadvisor-" + today + ".html"
        self.assertEqual(filename, check_file)
        self.assertTrue(os.path.isfile(check_file))

if __name__ == '__main__':
    unittest.main()
