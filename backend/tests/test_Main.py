from src.ParseText import parser
from src.Search import Search
from src import Course
from Main import main as mainLoop

import filecmp
import os

from unittest.mock import patch
from unittest import TestCase
import unittest


class MainTest(TestCase):
    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '13'])
    def test_quit(self, input):
        mainLoop()

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '1', '1', '1', '1', '13'])
    def test_weights(self, input):
        mainLoop()

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '2', '86', '1', '1', '13'])
    def test_department(self, input):
        mainLoop()

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '3', '1000', '1', '1', '13'])
    def test_codes(self, input):
        mainLoop()

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '4', '1', '1', '1', '13'])
    def test_semester(self, input):
        mainLoop()

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '5', '1', '1', '1', '13'])
    def test_level(self, input):
        mainLoop()

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '2', '17', '2', '1', '3', '2', '4', '4', '1', '3', 'cis75FW', '13'])
    def test_multisearch(self, input):
        mainLoop()
        
        data_dir = os.path.dirname(os.getcwd()) + '/backend/export/'
        test_dir = os.path.dirname(os.getcwd()) + '/backend/tests/export/'
        assert os.path.exists(data_dir + "Edgescis75FWTable.csv")
        assert os.path.exists(data_dir + "Nodescis75FWTable.csv")

        try:
            #This tests to make sure the files created files are the same as the test files
            self.assertEqual(True, filecmp.cmp(data_dir + "Edgescis75FWTable.csv", test_dir + "Edgescis75FWTable.csv"))
            self.assertEqual(True, filecmp.cmp(data_dir + "Nodescis75FWTable.csv", test_dir + "Nodescis75FWTable.csv"))
        except Exception as e:
            self.assertTrue(False, e)

        os.remove(data_dir + "Edgescis75FWTable.csv")
        os.remove(data_dir + "Nodescis75FWTable.csv")

if __name__ == '__main__':
    unittest.main()
