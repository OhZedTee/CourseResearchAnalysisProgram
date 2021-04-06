from src.UserInterface import UserInterface
from src.ParseFactory import ParseFactory
from Main import main as mainLoop
import filecmp

import os

from unittest.mock import patch
from unittest import TestCase
import unittest

#For testing, just CIS courses and much smaller data set
data_dir = os.getcwd()
testing_CIS_file = data_dir + "/tests/data/" + "Section_Selection_Results___WebAdvisor___University_of_Guelph.html"

class ParseFactoryTest(TestCase):
    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '11'])
    def test_parse_factory(self, input):
        userInterface = UserInterface()
        factory = ParseFactory(userInterface, testing_CIS_file)

        for key in factory.webData:
            if factory.webData[key].courseKey != None:
                self.assertEqual(factory.webData[key].courseKey, factory.textData[factory.webData[key].courseKey].to_hash())

if __name__ == '__main__':
    unittest.main()
