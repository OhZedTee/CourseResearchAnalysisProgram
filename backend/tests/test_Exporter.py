from src.ParseText import parser
from src.Search import Search
from src import Course
from Main import main as mainLoop
from src.Exporter import Exporter
import filecmp

import os
import re

from unittest.mock import patch
from unittest import TestCase
import unittest

class ExporterTest(TestCase):

    data_dir = os.path.dirname(os.getcwd()) + '/backend/export/'
    edge_file = data_dir + "EdgesSummaryTable.csv"
    node_file = data_dir + "NodesSummaryTable.csv"

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '1', '1', '1', '2', 'Summary', '13'])
    def test_export_node_success(self, input):
        mainLoop()

        assert os.path.exists(self.node_file)

        try:
            file = open(self.node_file, "r")

            header = file.readline()

            # if line is empty
            # end of file is reached
            if not header:
                self.assertTrue(False, "NodeTable.csv file is empty")

            if "Id,Label,Department" not in header:
                self.assertTrue(False, "NodeTable.csv not formatted correctly")

            for line in file:
                # Match format (anything,"anything")
                if not re.match(r'^.+,\".+\",\".+\"$', line):
                    self.assertTrue(False, "NodeTable.csv not formatted correctly: \n" + line)


            file.close()
        except:
            self.assertTrue(False, "Couldn't open NodeTable.csv, does not exist")
        os.remove(self.edge_file)
        os.remove(self.node_file)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '1', '1', '1', '2', 'Summary', '13'])
    def test_export_edge_success(self, input):
        mainLoop()

        assert os.path.exists(self.edge_file)

        try:
            file = open(self.edge_file, "r")

            header = file.readline()

            # if line is empty
            # end of file is reached
            if not header:
                self.assertTrue(False, "EdgeTable.csv file is empty")

            if "Source,Target" not in header:
                self.assertTrue(False, "EdgeTable.csv not formatted correctly")

            for line in file:
                # Match format (anything,anything)
                if not re.match(r'^.+,.+$', line):
                    self.assertTrue(False, "EdgeTable.csv not formatted correctly: \n" + line)


            file.close()
        except:
            self.assertTrue(False, "Couldn't open EdgeTable.csv, does not exist")
        os.remove(self.edge_file)
        os.remove(self.node_file)