from src.PickleToFile import PickleToFile
from pathlib import Path

import os
import re

from unittest.mock import patch
from unittest import TestCase
import unittest

class PickleTestCase(TestCase):

    data_dir = os.getcwd()
    pickleObj = PickleToFile(data_dir + "/tests/testFileDir/testCreateFile.txt")
    testObjToSave = {"test": "test"}

    def test_writing_to_file(self):
        #Saving an object to a file, then checking if the file exists and if it is not empty
        self.pickleObj.pickleObjectToFile(self.testObjToSave)
        assert os.path.exists(self.data_dir + "/tests/testFileDir/testCreateFile.txt")
        self.assertTrue((Path(self.data_dir + "/tests/testFileDir/testCreateFile.txt").stat().st_size > 0), True)

    def test_reading_from_file(self):
        #saving to file from original test
        self.pickleObj.pickleObjectToFile(self.testObjToSave)
        assert os.path.exists(self.data_dir + "/tests/testFileDir/testCreateFile.txt")
        self.assertTrue((Path(self.data_dir + "/tests/testFileDir/testCreateFile.txt").stat().st_size > 0), True)
        #Retrieving the object stored in the first test case, then checking to make sure it's
        #the same as the object that was saved
        newObj = self.pickleObj.retrievePickledObject()
        self.assertTrue(self.testObjToSave, newObj)
