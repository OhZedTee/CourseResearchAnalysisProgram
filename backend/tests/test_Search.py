from src.ParseText import parser
from src.Search import Search
from src import Course
from src.UserInterface import UserInterface
from Main import main as mainLoop
from src.ParseFactory import ParseFactory
from src.PickleToFile import PickleToFile

import filecmp
import os

from unittest.mock import patch
from unittest import TestCase
import unittest

#For testing, just CIS courses and much smaller data set
data_dir = os.getcwd()
testing_CIS_file = data_dir + "/tests/data/" + "Section_Selection_Results___WebAdvisor___University_of_Guelph.html"

@patch('src.UserInterface.get_input', return_value='othertestcases.txt')
def setup_ui(self, input):
    return UserInterface()

class SearchTest(TestCase):
    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '13'])
    def test_quit(self, input):
        userInterface = UserInterface()
        courseTable = parser(userInterface.filename)
        keys = courseTable.keys()
        search = Search(userInterface, keys, None)
        matches = search.findKeys()
        self.assertEqual("quit", matches)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '3', '4550'])
    def test_course_code(self, input):
        userInterface = UserInterface()
        courseTable = parser(userInterface.filename)
        keys = courseTable.keys()
        search = Search(userInterface, keys, None)
        matches = search.findKeys()
        correct = True
        for m in matches:
            if (m.split("-")[1] != '4550'):
                correct = False
        self.assertEqual(correct, True)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '2', '86'])
    def test_course_department(self, input):
        userInterface = UserInterface()
        courseTable = parser(userInterface.filename)
        keys = courseTable.keys()
        search = Search(userInterface, keys, None)
        matches = search.findKeys()
        correct = True
        for m in matches:
            if (m.split("-")[0] != 'ZOO'):
                correct = False
        self.assertEqual(correct, True)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '4', '1'])
    def test_course_semester(self, input):
        userInterface = UserInterface()
        courseTable = parser(userInterface.filename)
        keys = courseTable.keys()
        search = Search(userInterface, keys, None)
        matches = search.findKeys()
        correct = True
        for m in matches:
            if (m.split("-")[2].find('F') == -1):
                correct = False
        self.assertEqual(correct, True)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '1', '1'])
    def test_course_weight(self, input):
        userInterface = UserInterface()
        courseTable = parser(userInterface.filename)
        keys = courseTable.keys()
        search = Search(userInterface, keys, None)
        matches = search.findKeys()
        correct = True
        for m in matches:
            if (m.split("-")[3] != '0.25'):
                correct = False
        self.assertEqual(correct, True)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '5', '4'])
    def test_course_level(self, input):
        userInterface = UserInterface()
        courseTable = parser(userInterface.filename)
        keys = courseTable.keys()
        search = Search(userInterface, keys, None)
        matches = search.findKeys()
        correct = True
        for m in matches:
            if (m.split("-")[1][0] != '4'):
                correct = False
        self.assertEqual(correct, True)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '6', 'CIS*1500'])
    def test_full_course_level(self, input):
        userInterface = UserInterface()
        courseTable = parser(userInterface.filename)
        keys = courseTable.keys()
        search = Search(userInterface, keys, None)
        matches = search.findKeys()
        correct = True
        for m in matches:
            if (m.split("-")[1] != '1500'):
                correct = False
        self.assertEqual(correct, True)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '7', '1'])
    def test_search_availability(self, input):
        userInterface = UserInterface()
        factory = ParseFactory(userInterface, testing_CIS_file)
        search = Search(userInterface, factory.textData.keys(), factory.webData)
        matches = search.findKeys()
        courses = ['CIS-1050-S,W-0.50', 'CIS-1200-F,W-0.50', 'CIS-1500-F,W-0.50', 'CIS-2250-W-0.50', 
                   'CIS-2500-W-0.50', 'CIS-2750-W-0.75', 'CIS-3110-W-0.50', 'CIS-3120-W-0.50', 'CIS-3190-W-0.50', 'CIS-3490-W-0.50', 
                   'CIS-3700-W-0.50', 'CIS-3750-F,W-0.75', 'CIS-3760-F,W-0.75', 'CIS-4030-W-0.50', 'CIS-4250-W-0.50', 'CIS-4520-W-0.50', 
                   'CIS-4720-W-0.50', 'CIS-4820-W-0.50', 'CIS-4900-S,F,W-0.50', 'CIS-4910-S,F,W-0.50']
        self.assertEqual(matches, courses)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '11', '50'])
    def test_search_capacity_max(self, input):
        userInterface = UserInterface()
        factory = ParseFactory(userInterface, testing_CIS_file)
        search = Search(userInterface, factory.textData.keys(), factory.webData)
        matches = search.findKeys()
        courses = ['CIS-4900-S,F,W-0.50', 'CIS-4910-S,F,W-0.50']
        self.assertEqual(matches, courses)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '12', '50'])
    def test_search_capacity_min(self, input):
        userInterface = UserInterface()
        factory = ParseFactory(userInterface, testing_CIS_file)
        search = Search(userInterface, factory.textData.keys(), factory.webData)
        matches = search.findKeys()
        courses = ['CIS-1050-S,W-0.50', 'CIS-1200-F,W-0.50', 'CIS-1500-F,W-0.50', 'CIS-2170-W-0.75', 'CIS-2250-W-0.50', 
                    'CIS-2500-W-0.50', 'CIS-2750-W-0.75', 'CIS-2910-W-0.50', 'CIS-3110-W-0.50', 'CIS-3120-W-0.50', 'CIS-3190-W-0.50',
                    'CIS-3490-W-0.50', 'CIS-3700-W-0.50', 'CIS-3750-F,W-0.75', 'CIS-3760-F,W-0.75', 'CIS-4030-W-0.50', 'CIS-4250-W-0.50', 
                    'CIS-4520-W-0.50', 'CIS-4650-W-0.50', 'CIS-4720-W-0.50', 'CIS-4820-W-0.50']
        self.assertEqual(matches, courses)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '8', 'Klotz'])
    def test_search_faculty(self, input):
        userInterface = UserInterface()
        factory = ParseFactory(userInterface, testing_CIS_file)
        search = Search(userInterface, factory.textData.keys(), factory.webData)
        matches = search.findKeys()
        courses = ['CIS-4250-W-0.50']
        self.assertEqual(matches, courses)

    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '9'])
    def test_dropped_courses(self, input):
        userInterface = UserInterface()
        factory = ParseFactory(userInterface, testing_CIS_file)

        pickle = PickleToFile("data/saved-webscrape.txt")
        pickle.pickleObjectToFile(factory.webData)

        search = Search(userInterface, factory.textData.keys(), factory.webData)
        matches = search.findKeys()
        self.assertEqual(matches, [])



    @patch('src.UserInterface.get_input', side_effect=['course-descriptions.txt', '10'])
    def test_current_semester(self, input):
        userInterface = UserInterface()
        courseTable = parser(userInterface.filename)
        keys = courseTable.keys()
        search = Search(userInterface, keys, None)
        matches = search.findKeys()
        notCurrent = ['ACCT-4230-W-0.50', 'ACCT-4290-W-0.50', 'ACCT-4340-W-0.50', 'ACCT-1220-F,W-0.50', 'ACCT-1240-W-0.50', 'ACCT-2230-F,W-0.50', 'ACCT-3230-S,W-0.50', 'ACCT-3330-F,W-0.50', 'ACCT-4440-W-0.50', 'AGR-2500-W-0.50', 'AGR-3010-S,F,W-0.50', 'AGR-4010-S,F,W-0.50', 'AGR-2050-W-0.50', 'AGR-4450-S,F,W-1.00', 'AGR-4460-S,F,W-1.00', 'AGR-4600-W-1.00', 'ANSC-3170-W-0.50', 'ANSC-3180-W-0.50', 'ANSC-3270-W-0.50', 'ANSC-4090-W-0.50', 'ANSC-4100-W-0.50', 'ANSC-4260-W-0.50', 'ANSC-1210-W-1.00', 'ANSC-2340-W-0.50', 'ANSC-3040-W-0.50', 'ANSC-4350-W-0.50', 'ANSC-4470-W-0.50', 'ANSC-4490-W-0.50', 'ANSC-4610-W-0.50', 'ANSC-4650-W-0.50', 'ANSC-4700-S,F,W-0.50', 'ANSC-4710-S,F,W-0.50', 'ANTH-3770-W-0.50', 'ANTH-3840-F,W-0.50', 'ANTH-3850-F,W-0.50', 'ANTH-3950-S,F,W-0.50', 'ANTH-4440-W-0.50', 'ANTH-4540-F,W-0.50', 'ANTH-1150-F,W-0.50', 'ANTH-2180-W-0.50', 'ANTH-2660-W-0.50', 'ANTH-3550-W-0.50', 'ANTH-4640-F,W-0.50', 'ANTH-4700-W-0.50', 'ANTH-4740-F,W-0.50', 'ANTH-4840-F,W-0.50', 'ANTH-4880-S,F,W-0.50', 'ANTH-4890-S,F,W-0.50', 'ANTH-4900-S,F,W-0.50', 'ANTH-4910-S,F,W-0.50', 'ARAB-1110-W-0.50', 'ARTH-2280-W-0.50', 'ARTH-2550-W-0.50', 'ARTH-2600-W-0.50', 'ARTH-1520-W-0.50', 'ARTH-2070-W-0.50', 'ARTH-2120-W-0.50', 'ARTH-2950-W-0.50', 'ARTH-3060-W-0.50', 'ARTH-3150-W-0.50', 'CLAS-3150-W-0.50', 'ARTH-3600-W-0.50', 'ARTH-3210-W-0.50', 'ARTH-3320-W-0.50', 'ARTH-3780-W-0.50', 'ARTH-4310-W-1.00', 'ARTH-4330-W-1.00', 'ARTH-4600-S,F,W-0.50', 'ARTH-4800-F,W-0.50', 'ASCI-4010-W-1.00', 'ASCI-4020-F,W-0.50', 'ASCI-4030-F,W-0.50', 'ASCI-4700-S,F,W-0.50', 'ASCI-4710-S,F,W-0.50', 'ASCI-1120-W-0.50', 'ASCI-3100-W-0.50', 'ASCI-3700-S,F,W-0.50', 'BIOC-2580-S,F,W-0.50', 'BIOC-3560-S,F,W-0.50', 'BIOC-4540-W-0.75', 'BIOC-4580-W-0.50', 'BIOL-2060-S,F,W-0.50', 'BIOL-2400-F,W-0.50', 'BIOL-3040-W-0.50', 'BIOL-1070-F,W-0.50', 'BIOL-1080-F,W-0.50', 'BIOL-1090-F,W-0.50', 'BIOL-1500-F,W-0.50', 'BIOL-3060-W-0.50', 'BIOL-3130-W-0.50', 'BIOL-3650-W-0.50', 'BIOL-3660-S,F,W-0.50', 'BIOL-3670-W-0.50', 'BIOL-4020-F,W-1.00', 'BIOL-4120-W-0.50', 'BIOL-4500-W-0.50', 'BIOL-4710-S,F,W-0.25', 'BIOL-4800-S,F,W-0.50', 'BIOL-4810-S,F,W-0.25', 'BIOL-4900-S,F,W-0.50', 'BIOM-3200-S,F,W-1.00', 'BIOM-4030-W-0.50', 'BIOM-4050-W-0.50', 'BIOM-4090-S,F,W-0.50', 'BIOM-2000-F,W-0.50', 'BIOM-3040-W-0.75', 'BIOM-3090-S,F,W-0.50', 'BIOM-4110-W-0.50', 'BIOM-4150-W-0.50', 'BIOM-4180-W-0.50', 'BIOM-4500-S,F,W-0.50', 'BIOM-4510-S,F,W-1.00', 'BIOM-4522-W-1.00', 'BOT-4380-W-0.50', 'BOT-1200-W-0.50', 'BOT-2000-W-0.50', 'BOT-3310-W-0.50', 'BOT-3710-W-0.50', 'BUS-4550-S,F,W-0.50', 'BUS-4560-S,F,W-0.50', 'CHEM-2700-S,W-0.50', 'CHEM-3360-S,W-0.50', 'CHEM-1050-F,W-0.50', 'CHEM-1100-W-0.50', 'CHEM-2070-S,W-0.50', 'CHEM-2400-S,F,W-0.75', 'CHEM-2480-S,F,W-0.50', 'CHEM-3430-S,F,W-0.50', 'CHEM-3650-W-0.50', 'CHEM-3760-W-0.50', 'CHEM-3870-W-0.50', 'CHEM-4010-W-0.50', 'CHEM-4400-W-0.50', 'CHEM-4630-W-0.50', 'CHEM-4880-W-0.50', 'CHEM-4900-S,F,W-1.00', 'CHEM-4910-S,F,W-1.00', 'CHEM-4720-W-0.50', 'CHIN-1210-W-0.50', 'CHIN-1290-W-0.50', 'CHIN-2210-W-0.50', 'CLAS-3040-W-0.50', 'CLAS-3070-World-1.00', 'CLAS-1000-F,W-0.50', 'CLAS-2000-W,S-0.50', 'CLAS-2350-W-0.50', 'CLAS-3010-W-0.50', 'CLAS-3030-W-0.50', 'CLAS-3700-S,F,W-0.50', 'CLAS-4150-F,W-0.50', 'CLAS-4400-W-0.50', 'CIS-2170-W-0.75', 'CIS-2250-W-0.50', 'CIS-2500-W-0.50', 'CIS-2750-W-0.75', 'CIS-2910-W-0.50', 'CIS-1000-S,F,W-0.50', 'CIS-1050-S,W-0.50', 'CIS-1200-F,W-0.50', 'CIS-1500-F,W-0.50', 'CIS-3110-W-0.50', 'CIS-3120-W-0.50', 'CIS-3190-W-0.50', 'CIS-3490-W-0.50', 'CIS-3700-W-0.50', 'CIS-3750-F,W-0.75', 'CIS-3760-F,W-0.75', 'CIS-4010-W-0.50', 'CIS-4030-W-0.50', 'CIS-4250-W-0.50', 'CIS-4520-W-0.50', 'CIS-4650-W-0.50', 'CIS-4720-W-0.50', 'CIS-4800-W-0.50', 'CIS-4820-W-0.50', 'CIS-4900-S,F,W-0.50', 'CIS-4910-S,F,W-0.50', 'COOP-XXXX-F,W-0.00', 'COOP-1000-F,W,S-0.50', 'COOP-2000-F,W,S-0.50', 'COOP-3000-F,W,S-0.50', 'COOP-4000-F,W,S-0.50', 'COOP-5000-F,W,S-0.50', 'CROP-3300-W-0.50', 'CROP-4220-W-0.50', 'CTS-2000-W-0.50', 'ECON-2740-F,W-0.50', 'ECON-2770-F,W-0.50', 'ECON-3100-W-0.50', 'ECON-3500-W-0.50', 'ECON-1050-S,F,W-0.50', 'ECON-1100-S,F,W-0.50', 'ECON-2310-S,F,W-0.50', 'ECON-2410-S,F,W-0.50', 'ECON-2420-W-0.50', 'ECON-2720-W-0.50', 'ECON-3610-W-0.50', 'ECON-3710-F,W-0.50', 'ECON-3730-W-0.50', 'ECON-3740-F,W-0.50', 'ECON-3810-W-0.50', 'ECON-3900-S,F,W-0.50', 'ECON-4400-W-0.50', 'ECON-4810-W-0.50', 'ECON-4830-W-0.50', 'ECON-4900-S,F,W-0.50', 'ECON-4910-S,F,W-0.50', 'EDRD-3400-W-0.50', 'EDRD-3500-F,W-0.50', 'UNIV-3500-W-0.50', 'EDRD-2650-W-0.50', 'REXT-3100-W-0.50', 'REXT-4100-W-0.50', 'REXT-3040-W-0.50', 'ENGG-2180-W-0.50', 'ENGG-2230-F,W-0.50', 'ENGG-2340-W-0.50', 'ENGG-1210-W-0.50', 'ENGG-1500-F,W-0.50', 'ENGG-2100-F,W-0.75', 'ENGG-2120-F,W-0.50', 'ENGG-2450-W-0.50', 'ENGG-2550-W-0.50', 'ENGG-2560-W-0.50', 'ENGG-2660-W-0.50', 'ENGG-3100-W-0.75', 'ENGG-3120-W-0.75', 'ENGG-3130-W-0.50', 'ENGG-3170-W-0.50', 'ENGG-3190-W-0.50', 'ENGG-3210-W-0.50', 'ENGG-3220-W-0.50', 'MATH-1210-W-0.50', 'ENGG-3370-W-0.50', 'ENGG-3380-W-0.50', 'ENGG-3410-W-0.50', 'ENGG-3430-W-0.50', 'ENGG-3440-W-0.50', 'ENGG-3470-W-0.50', 'ENGG-3490-W-0.75', 'ENGG-4030-W-0.75', 'ENGG-4050-W-0.50', 'ENGG-4060-W-0.50', 'ENGG-4070-W-0.50', 'ENGG-4090-W-0.75', 'ENGG-4110-F,W-1.00', 'ENGG-4120-F,W-1.00', 'ENGG-4130-F,W-1.00', 'ENGG-4150-F,W-1.00', 'ENGG-4160-F,W-1.00', 'ENGG-4170-F,W-1.00', 'ENGG-4180-F,W-1.00', 'ENGG-4220-W-0.75', 'ENGG-4250-W-0.75', 'ENGG-4300-W-0.75', 'ENGG-4400-W-0.75', 'ENGG-4430-W-0.50', 'ENGG-4440-W-0.50', 'ENGG-4480-W-0.75', 'ENGG-4490-W-0.75', 'ENGG-4510-W-0.50', 'ENGG-4540-W-0.50', 'ENGG-4550-W-0.50', 'ENGG-4560-W-0.75', 'ENGG-4580-W-0.75', 'ENGG-4660-W-0.50', 'ENGG-4680-W-0.75', 'ENGG-4720-W-0.50', 'ENGG-4760-W-0.50', 'ENGG-4820-W-0.50', 'ENGL-1500-W-0.50', 'ENGL-2080-F,W-0.50', 'ENGL-2090-W-0.50', 'ENGL-2120-F,W-0.50', 'ENGL-2130-F,W-0.50', 'ENGL-1080-S,F,W-0.50', 'ENGL-1200-F,W-0.50', 'ENGL-2190-W-0.50', 'ENGL-2280-W-0.50', 'ENGL-2290-W-0.50', 'ENGL-2360-W-0.50', 'ENGL-2550-W-0.50', 'ENGL-2740-F,W-0.50', 'ENGL-2880-W-0.50', 'ENGL-2920-F,W-0.50', 'ENGL-3050-F,W-0.50', 'ENGL-3070-W-0.50', 'ENGL-3080-W-0.50', 'ENGL-3090-F,W-0.50', 'ENGL-3240-W-0.50', 'ENGL-3380-W-0.50', 'ENGL-3420-W-0.50', 'ENGL-3470-W-0.50', 'ENGL-3540-W-0.50', 'ENGL-3550-W-0.50', 'ENGL-3630-W-0.50', 'ENGL-3750-W-0.50', 'ENGL-3760-W-0.50', 'ENGL-3940-F,W-0.50', 'ENGL-3960-F,W-0.50', 'ENGL-4720-F,W-1.00', 'ENGL-4810-S,F,W-0.50', 'ENGL-4910-S,F,W-0.50', 'ENVM-3500-W-1.00', 'ENVS-2080-W-0.50', 'ENVS-2090-W-0.50', 'ENVS-2130-F,W-0.50', 'ENVS-2210-F,W-0.50', 'ENVS-2230-F,W-0.50', 'ENVS-1060-S,F,W-0.50', 'ENVS-2040-W-0.50', 'ENVS-2250-S,W-0.50', 'ENVS-2270-F,W-0.50', 'ENVS-2310-W-0.50', 'ENVS-3000-F,W-0.50', 'ENVS-3050-W-0.50', 'ENVS-3060-W-0.50', 'AGR-2320-W-0.50', 'HORT-2450-W-0.50', 'ENVS-3300-W-0.50', 'ENVS-3310-W-0.50', 'ENVS-3370-W-0.50', 'ENVS-4000-W-0.50', 'ENVS-3150-W-0.50', 'ENVS-4002-W-0.50', 'ENVS-4030-W-0.50', 'ENVS-4070-W-0.50', 'ENVS-4100-W-0.50', 'ENVS-4190-W-0.50', 'ENVS-4210-W-0.50', 'ENVB-3090-F,W-0.50', 'ENVS-4360-W-0.50', 'ENVS-4370-W-0.50', 'ENVS-4410-S,F,W-0.50', 'ENVS-4420-S,F,W-0.50', 'ENVS-4430-S,F,W-1.00', 'ENVS-4510-S,F,W-0.50', 'EQN-3060-W-0.50', 'EQN-3070-W-0.50', 'EQN-4020-W-0.50', 'EQN-2040-W-0.50', 'EQN-2050-W-0.50', 'EURO-4740-F,W-0.50', 'EURO-2200-W-0.50', 'EURO-3000-W-0.50', 'EURO-3700-S,F,W-0.50', 'EURO-4600-W-0.50', 'XSEN-3200-W-0.50', 'XSEN-3210-W-0.50', 'XSEN-XXXX-W-0.50', 'XSEN-3040-W-0.50', 'XSEN-3060-W-0.50', 'XSEN-3070-W-0.50', 'XSEN-3090-W-0.50', 'FIN-3500-W-0.50', 'FIN-4000-W-0.50', 'FIN-4100-W-0.50', 'FIN-4900-S,F,W-0.50', 'FIN-2000-S,F,W-0.50', 'FIN-3000-F,W-0.50', 'FIN-3100-F,W-0.50', 'FIN-3200-W-0.50', 'FRHD-2260-W-0.50', 'FRHD-2280-F,W-0.50', 'FRHD-2400-W-0.50', 'FRHD-3040-W-0.50', 'FRHD-1010-F,W-0.50', 'FRHD-1020-W-0.50', 'FRHD-2040-W-0.50', 'FRHD-2100-F,W-0.50', 'FRHD-3090-F,W-0.50', 'FRHD-3150-W-0.50', 'FRHD-3190-S,W-0.50', 'FRHD-3200-F,W-1.00', 'FRHD-3250-F,W-1.00', 'FRHD-3290-F,W-1.00', 'FRHD-3400-F,W-0.50', 'FRHD-3500-S,F,W-0.50', 'FRHD-4200-W-0.50', 'FRHD-4250-W-0.50', 'FRHD-4260-W-0.50', 'FRHD-4290-F,W-1.00', 'FRHD-4320-W-0.50', 'FRHD-4330-F,W-1.00', 'FRHD-4340-F,W-1.00', 'FRHD-4350-F,W-1.00', 'FRHD-4400-W-0.50', 'FARE-3310-F,W-0.50', 'FARE-4000-W-0.50', 'FARE-4220-W-0.50', 'FARE-1040-W-1.00', 'FARE-1300-W-0.50', 'FARE-1400-W-1.00', 'FARE-2410-W-0.50', 'FARE-4240-W-0.50', 'FARE-4310-W-0.50', 'FARE-4330-W-0.50', 'FARE-4360-W-0.50', 'FARE-4380-W-0.50', 'FARE-4550-S,F,W-0.50', 'FARE-4560-S,F,W-0.50', 'FOOD-3040-W-0.50', 'FOOD-3060-W-0.50', 'FOOD-2010-S,W-0.50', 'FOOD-2100-W-0.50', 'FOOD-2620-W-0.50', 'FOOD-3170-W-0.50', 'FOOD-3260-W-0.50', 'FOOD-3270-W-0.50', 'FOOD-4020-W-0.50', 'FOOD-4090-W-0.50', 'FOOD-4110-W-0.50', 'FOOD-4220-S,F,W-0.50', 'FOOD-4230-S,F,W-0.50', 'FOOD-4270-W-0.50', 'FOOD-4310-W-0.50', 'FOOD-4400-W-0.50', 'FREN-2020-F,W-0.50', 'FREN-2060-F,W-0.50', 'FREN-2500-W-0.50', 'FREN-2520-F,W-0.50', 'FREN-2550-W-0.50', 'FREN-3090-W-0.50', 'FREN-3110-W-0.50', 'FREN-1100-F,W-0.50', 'FREN-1150-F,W-0.50', 'FREN-1300-F,W-0.50', 'FREN-3140-W-0.50', 'FREN-3520-W-0.50', 'FREN-3610-F,W-0.50', 'FREN-3620-F,W-0.50', 'FREN-3630-F,W-0.50', 'FREN-3640-F,W-0.50', 'FREN-3650-F,W-0.50', 'FREN-3660-F,W-0.50', 'FREN-3670-F,W-0.50', 'FREN-3680-F,W-0.50', 'FREN-3690-F,W-0.50', 'FREN-3700-S,F,W-0.50', 'FREN-4020-W-0.50', 'FREN-3120-W-0.50', 'FREN-4740-S,F,W-0.50', 'FREN-4770-S,F,W-0.50', 'GEOG-2210-W-0.50', 'GEOG-2260-W-0.50', 'GEOG-2480-F,W-0.50', 'GEOG-2510-W-0.50', 'GEOG-1220-F,W-0.50', 'GEOG-1300-F,W-0.50', 'GEOG-1350-F,W-0.50', 'GEOG-2110-W-0.50', 'GEOG-3050-W-0.50', 'GEOG-3420-W-0.50', 'GEOG-3480-F,W-0.50', 'GEOG-3490-S,F,W-0.50', 'GEOG-3610-W-0.50', 'GEOG-4150-W-0.50', 'GEOG-4220-W-0.50', 'GEOG-4230-W-0.50', 'GEOG-4390-W-0.50', 'GEOG-4480-W-1.00', 'GEOG-4880-W-0.50', 'GEOG-4990-S,F,W-0.50', 'GERM-2010-F,W-0.50', 'GERM-1110-W-0.50', 'GERM-3000-W-0.50', 'GERM-3700-S,F,W-0.50', 'GREK-2020-W-0.50', 'HIST-2070-W-0.50', 'HIST-2090-W-0.50', 'HIST-2120-W-0.50', 'HIST-2160-W-0.50', 'HIST-2190-W-0.50', 'HIST-1010-S,F,W-0.50', 'HIST-1050-F,W-0.50', 'HIST-1150-F,W-0.50', 'HIST-1250-F,W-0.50', 'HIST-2020-W-0.50', 'HIST-2040-W-0.50', 'HIST-2250-W-0.50', 'HIST-2260-W-0.50', 'HIST-2340-W-0.50', 'HIST-2600-W-0.50', 'HIST-2850-W-0.50', 'HIST-2910-W-0.50', 'HIST-2920-W-0.50', 'HIST-3070-W-0.50', 'HIST-3270-W-0.50', 'HIST-3330-W-0.50', 'HIST-3360-W-0.50', 'HIST-3460-W-0.50', 'HIST-3490-W-0.50', 'HIST-3520-W-0.50', 'HIST-3560-F,W-0.50', 'HIST-3830-W-0.50', 'HIST-3840-W-0.50', 'HIST-3910-W-0.50', 'HIST-4010-W-1.00', 'HIST-4070-S,F,W-1.00', 'HIST-4170-W-1.00', 'HIST-4270-W-1.00', 'HORT-3280-W-0.50', 'HORT-3310-W-0.50', 'HORT-3430-W-0.50', 'HORT-4200-W-0.50', 'HORT-4300-W-0.50', 'HORT-1120-W-0.50', 'HORT-3270-W-0.50', 'HORT-4450-W-0.50', 'HTM-2070-W-0.50', 'HTM-2700-F,W-0.50', 'HTM-1160-W-0.50', 'HTM-2010-F,W-0.50', 'HTM-2020-W-0.50', 'HTM-2030-F,W-0.50', 'HTM-3080-F,W-0.50', 'HTM-3090-F,W-1.00', 'HTM-3120-F,W-0.50', 'HTM-3180-W-0.50', 'HTM-3220-W-0.50', 'HTM-3780-W-0.50', 'FOOD-2010-W-0.50', 'HTM-4050-W-0.50', 'HTM-4060-W-0.50', 'HTM-4080-F,W-0.50', 'HTM-4110-W-0.50', 'HTM-4170-W-0.50', 'HTM-4190-F,W-0.50', 'HTM-4250-F,W-0.50', 'HROB-3090-W-0.50', 'HROB-3100-F,W-0.50', 'HROB-4000-W-0.50', 'HROB-4010-W-0.50', 'ManagementHROB-2010-F,W-0.50', 'BUS-2010-F,W-0.50', 'HROB-2290-F,W-0.50', 'HROB-3030-W-0.50', 'HROB-4060-W-0.50', 'HK-3502-W-0.75', 'HK-2810-W-0.50', 'HK-3100-W-0.50', 'HK-3402-W-0.75', 'HK-4070-W-0.50', 'HK-4230-S,F,W-0.50', 'HK-4240-W-0.75', 'HK-4360-S,F,W-1.00', 'HK-4371-S,F,W-0.50', 'HK-4372-F,W,S-0.50', 'HK-4442-W-1.00', 'HK-4460-W-0.50', 'HK-4510-S,F,W-1.00', 'HK-4511-S,F,W-0.50', 'HK-4512-S,F,W-0.50', 'HK-4600-W-0.75', 'HUMN-3180-W-0.50', 'HUMN-3190-S,F,W-0.50', 'HUMN-3240-W-0.50', 'HUMN-3300-F,W-0.50', 'HUMN-1300-W-0.50', 'HUMN-2020-W-0.50', 'HUMN-3000-W-0.50', 'HUMN-3100-W-0.50', 'HUMN-3150-W-0.50', 'HUMN-4190-S,F,W-0.50', 'INDG-1100-W-0.50', 'IPS-1510-W-1.00', 'ISS-3100-W-0.50', 'ISS-3150-W-0.50', 'ISS-3270-W-0.50', 'ISS-3300-F,W-0.50', 'ISS-3420-W-0.50', 'UNIV-2800-S,F,W-0.50', 'UNIV-3000-W-0.50', 'UNIV-2010-F,W-0.50', 'UNIV-2020-F,W-0.50', 'UNIV-2100-F,W-0.50', 'UNIV-3140-F,W-0.50', 'UNIV-3150-W-0.50', 'UNIV-3160-W-0.50', 'UNIV-3170-W-0.50', 'UNIV-3800-S,F,W-0.50', 'UNIV-4410-W-0.50', 'UNIV-4800-S,F,W-0.50', 'IBIO-4522-W-1.00', 'IBIO-3100-W-0.50', 'IBIO-4500-F,W-1.00', 'IBIO-4510-F,W-1.00', 'IDEV-2500-W-0.50', 'IDEV-3100-W-0.50', 'IDEV-3010-F,W-0.50', 'IDEV-3200-S,F,W-0.50', 'IDEV-3300-F,W-0.50', 'IDEV-1000-S,F,W-0.50', 'IDEV-2300-S,W-0.50', 'IDEV-2400-W-0.50', 'IDEV-3400-W-0.50', 'IDEV-4000-F,W-1.00', 'IDEV-4100-S,F,W-0.50', 'IDEV-4150-S,F,W-0.50', 'IDEV-4600-S,F,W-0.50', 'IDEV-4190-S,F,W-0.25', 'IDEV-4200-S,F,W-0.75', 'ITAL-1060-F,W-0.50', 'ITAL-1070-W-0.50', 'ITAL-3060-W-0.50', 'ITAL-3700-S,F,W-0.50', 'ITAL-4900-F,W-0.50', 'LARC-3050-W-0.75', 'LARC-3430-W-0.50', 'LARC-3500-S,F,W-0.50', 'LARC-4090-W-0.50', 'LARC-2020-W-0.75', 'LARC-2230-W-0.50', 'LARC-2420-W-0.50', 'LARC-2820-W-0.50', 'LARC-4620-S,F,W-1.00', 'LARC-4710-W-1.00', 'LARC-4730-S,F,W-0.50', 'LARC-4740-S,F,W-0.50', 'LAT-1110-W-0.50', 'LAT-4150-F,W-0.50', 'LING-1000-F,W-0.50', 'LING-2400-W-0.50', 'MGMT-3020-S,F,W-0.50', 'MGMT-3030-W-0.50', 'MGMT-3300-F,W-0.50', 'MGMT-3320-S,F,W-0.50', 'MGMT-1100-F,W-0.00', 'MGMT-1200-W-0.50', 'MGMT-2150-S,F,W-0.50', 'MGMT-3400-S,F,W-0.50', 'MGMT-3500-F,W-0.50', 'MGMT-4000-F,W-0.50', 'MGMT-4030-W-0.50', 'MGMT-4040-W-0.50', 'MGMT-4050-F,W-0.50', 'MGMT-4060-F,W-0.50', 'MGMT-4200-W-0.50', 'MGMT-4260-W-0.50', 'MGMT-4300-W-0.50', 'MGMT-4500-W-0.50', 'MGMT-4991-S,F,W-1.00', 'MGMT-4992-S,F,W-1.00', 'MCS-3010-W-0.50', 'MCS-3030-F,W-0.50', 'MCS-3040-S,F,W-0.50', 'MCS-3050-F,W-0.50', 'MCS-3500-F,W-0.50', 'MCS-3600-F,W-0.50', 'MCS-1000-S,F,W-0.50', 'MCS-2000-S,F,W-0.50', 'MCS-2020-S,F,W-0.50', 'MCS-2100-S,F,W-0.50', 'COST-2100-F,W-0.50', 'MCS-3620-F,W-0.50', 'MCS-4300-W-0.50', 'MCS-4370-F,W-0.50', 'MCS-4600-F,W-0.50', 'MCS-4950-S,F,W-0.50', 'MATH-2130-W-0.50', 'MATH-2210-W-0.50', 'MATH-3100-W-0.50', 'MATH-1200-F,W-0.50', 'MATH-1080-F,W-0.50', 'MATH-1090-W-0.50', 'MATH-1160-F,W-0.50', 'MATH-3160-W-0.50', 'MATH-3260-W-0.50', 'MATH-3510-W-0.50', 'MATH-4050-W-0.50', 'MATH-4060-W-0.50', 'MATH-4150-F,W-0.50', 'MATH-4200-W-0.50', 'MATH-4310-W-0.50', 'MATH-4440-W-0.50', 'MATH-4600-F,W-1.00', 'MICR-3430-W-0.75', 'MICR-4330-W-0.50', 'MICR-4430-W-0.50', 'MICR-4530-W-0.50', 'MICR-2420-S,F,W-0.50', 'MICR-2430-F,W-0.50', 'MCB-4600-S,F,W-0.50', 'MCB-2050-F,W-0.50', 'MCB-3010-W-0.50', 'MCB-4010-W-0.50', 'MCB-4500-S,F,W-1.00', 'MCB-4510-S,F,W-1.00', 'MBG-3350-S,F,W-0.75', 'MBG-3660-W-0.50', 'MBG-4030-W-0.50', 'MBG-4240-W-0.50', 'MBG-1000-W-0.50', 'MBG-2040-F,W-0.50', 'MBG-3050-W-0.50', 'MBG-3060-W-0.50', 'MBG-3100-W-0.50', 'MBG-4270-W-0.50', 'MUSC-1510-S,F,W-0.50', 'MUSC-2100-F,W-0.50', 'MUSC-2140-F,W-0.50', 'MUSC-2150-F,W-0.50', 'MUSC-2180-F,W-0.50', 'MUSC-2220-W-0.50', 'MUSC-2270-W-0.50', 'MUSC-1130-F,W-0.50', 'MUSC-1180-F,W-0.50', 'MUSC-2330-W-0.50', 'MUSC-2420-W-0.50', 'MUSC-2500-S,F,W-0.50', 'MUSC-2510-S,F,W-0.50', 'MUSC-2530-F,W-0.25', 'MUSC-2540-F,W-0.25', 'MUSC-2550-F,W-0.25', 'MUSC-2560-F,W-0.25', 'MUSC-2580-F,W-0.25', 'MUSC-3210-F,W-0.25', 'MUSC-3220-F,W-0.25', 'MUSC-3230-F,W-0.25', 'MUSC-3240-F,W-0.25', 'MUSC-3410-F,W-0.50', 'MUSC-3420-F,W-0.50', 'MUSC-3500-S,F,W-0.50', 'MUSC-3510-S,F,W-0.50', 'MUSC-3550-F,W-0.25', 'MUSC-3560-F,W-0.25', 'MUSC-3800-W-1.00', 'MUSC-2100-W-1.00', 'MUSC-4200-S,F,W-0.50', 'MUSC-4450-W-1.00', 'MUSC-4460-S,F,W-0.50', 'MUSC-4470-S,F,W-0.50', 'NANO-4200-W-0.50', 'NANO-4900-W-0.50', 'NANO-4910-S,F,W-1.00', 'NANO-4920-S,F,W-1.00', 'NANO-2100-W-0.50', 'NANO-3300-W-0.50', 'NANO-3600-W-0.50', 'NEUR-4401-S,F,W-0.50', 'NEUR-4402-S,F,W-0.50', 'NEUR-4450-S,F,W-1.00', 'NEUR-3500-W-1.00', 'NUTR-3110-W-0.50', 'NUTR-3150-W-0.50', 'NUTR-3210-S,F,W-0.50', 'NUTR-1010-F,W-0.50', 'NUTR-1020-W-0.50', 'NUTR-3070-W-0.50', 'NUTR-3090-W-1.00', 'NUTR-4090-W-0.50', 'NUTR-4120-W-0.50', 'NUTR-4320-W-0.50', 'NUTR-4330-W-0.75', 'NUTR-4360-W-0.50', 'NUTR-4850-W-0.50', 'NUTR-4900-W-0.50', 'OAGR-2070-W-1.00', 'OAGR-4180-W-0.50', 'ONEH-1000-W-0.50', 'PATH-3040-W-0.50', 'PATH-3610-S,F,W-0.50', 'PHIL-2060-W-0.50', 'PHIL-2070-W-0.50', 'PHIL-2100-F,W-0.50', 'PHIL-2110-W-0.50', 'PHIL-2120-F,W-0.50', 'PHIL-1010-F,W-0.50', 'PHIL-1030-F,W-0.50', 'PHIL-1050-W-0.50', 'PHIL-2000-W-0.50', 'PHIL-2160-W-0.50', 'PHIL-2370-W-0.50', 'PHIL-2600-W-0.50', 'PHIL-3050-W-0.50', 'PHIL-3060-W-0.50', 'PHIL-3100-W-0.50', 'PHIL-3160-W-0.50', 'PHIL-3170-W-0.50', 'PHIL-3230-W-0.50', 'PHIL-3080-W-0.50', 'PHIL-3450-W-0.50', 'PHIL-3710-F,W-0.50', 'PHIL-3920-W-0.50', 'PHIL-4710-F,W-0.50', 'PHIL-4720-F,W-0.50', 'PHIL-4820-F,W-0.50', 'PHYS-2030-W-0.50', 'PHYS-2180-W-0.50', 'PHYS-2310-W-0.50', 'PHYS-1010-W-0.50', 'PHYS-1070-W-0.50', 'PHYS-1080-F,W-0.50', 'PHYS-2340-W-0.50', 'PHYS-3000-W-0.50', 'PHYS-3080-W-0.50', 'PHYS-3510-F,W-0.50', 'PHYS-4002-W-0.50', 'PHYS-4040-W-0.50', 'PHYS-4070-W-0.50', 'PHYS-4130-W-0.50', 'PHYS-4150-W-0.50', 'PHYS-4500-F,W-0.50', 'PHYS-4540-W-0.50', 'PBIO-4530-W-0.50', 'PBIO-4750-W-0.50', 'PBIO-3110-W-0.50', 'PBIO-4070-W-0.50', 'PBIO-4150-W-0.50', 'PBIO-4290-W-0.50', 'POLS-2250-W-0.50', 'POLS-2300-F,W-0.50', 'POLS-3050-W-0.50', 'POLS-1150-F,W-0.50', 'POLS-2100-W-0.50', 'POLS-2150-W-0.50', 'POLS-2230-F,W-0.50', 'POLS-3140-W-0.50', 'POLS-3210-S,W-0.50', 'POLS-3230-W-0.50', 'POLS-3650-W-0.50', 'POLS-3790-W-0.50', 'POLS-3890-W-0.50', 'POLS-3960-S,F,W-0.50', 'POLS-4060-F,W-0.50', 'POLS-4070-F,W-1.00', 'POLS-4140-W-1.00', 'POLS-4150-W-0.50', 'POLS-4250-W-1.00', 'POLS-4280-W-0.50', 'POLS-4300-W-1.00', 'POLS-4310-F,W-0.50', 'POLS-4730-W-1.00', 'POLS-4760-W-0.50', 'POLS-4780-F,W-0.50', 'POLS-4900-S,F,W-1.00', 'POLS-4910-S,F,W-0.50', 'POLS-4930-S,F,W-1.00', 'POLS-4970-S,F,W-0.50', 'POLS-4980-S,F,W-0.50', 'POPM-3240-F,W-0.50', 'PSYC-2070-F,W-0.50', 'PSYC-2310-S,F,W-0.50', 'PSYC-2360-F,W-0.50', 'PSYC-2390-W-0.50', 'PSYC-1010-F,W-0.50', 'PSYC-1500-F,W-0.50', 'PSYC-2020-W-0.50', 'PSYC-2650-W-0.50', 'PSYC-2740-W-0.50', 'PSYC-3000-F,W-0.50', 'PSYC-3030-W-0.50', 'PSYC-3110-W-0.50', 'PSYC-3250-F,W-0.50', 'PSYC-3290-F,W-0.50', 'PSYC-3300-W-0.50', 'PSYC-3410-W-0.50', 'PSYC-3450-W-0.50', 'PSYC-3470-W-0.50', 'PSYC-3910-F,W,S-0.50', 'PSYC-4240-S,F,W-0.50', 'PSYC-4310-W-0.50', 'PSYC-4460-W-0.50', 'PSYC-4540-F,W-1.00', 'PSYC-4750-W-0.50', 'PSYC-4870-S,F,W-0.50', 'PSYC-4880-S,F,W-1.00', 'REAL-4830-W-1.00', 'REAL-2820-W-0.50', 'REAL-3890-W-0.50', 'SOC-2700-F,W-0.50', 'SOC-2760-S,F,W-0.50', 'SOC-3380-W-0.50', 'SOC-3410-W-0.50', 'SOC-3490-W-0.50', 'SOC-3710-F,W-0.50', 'SOC-1500-F,W-0.50', 'SOC-2070-F,W-0.50', 'SOC-2080-W-0.50', 'SOC-3730-W-0.50', 'SOC-3750-F,W-0.50', 'SOC-3840-F,W-0.50', 'SOC-3850-F,W-0.50', 'SOC-3950-S,F,W-0.50', 'SOC-4010-F,W-0.50', 'SOC-4200-W-0.50', 'SOC-4410-F,W-0.50', 'SOC-4430-W-0.50', 'SOC-4740-F,W-0.50', 'SOC-4840-F,W-0.50', 'SOC-4880-S,F,W-0.50', 'SOC-4890-S,F,W-0.50', 'SOC-4900-S,F,W-0.50', 'SOC-4910-S,F,W-0.50', 'SOAN-3130-W-0.50', 'SOAN-3250-W-0.50', 'SOAN-3380-W-0.50', 'SOAN-4210-W-0.50', 'SOAN-2112-W-0.50', 'SOAN-2120-F,W-0.50', 'SOAN-3070-W-0.50', 'SOAN-4230-W-0.50', 'SOAN-4260-W-0.50', 'SOAN-4320-W-0.50', 'SOAN-4500-W-0.50', 'SPAN-3230-W-0.50', 'SPAN-3240-W-0.50', 'SPAN-1110-F,W-0.50', 'SPAN-2000-F,W-0.50', 'SPAN-2010-F,W-0.50', 'SPAN-2990-W-0.50', 'SPAN-3080-W-0.50', 'SPAN-3210-F,W-0.50', 'SPAN-3700-S,F,W-0.50', 'SPAN-4100-F,W-1.00', 'SPAN-4410-W-1.00', 'SPAN-4420-W-1.00', 'SPAN-4500-W-1.00', 'STAT-2230-W-0.50', 'STAT-3110-W-0.50', 'STAT-2040-S,F,W-0.50', 'STAT-2050-F,W-0.50', 'STAT-2060-F,W-0.50', 'STAT-2090-W-0.50', 'STAT-3510-W-0.50', 'STAT-4050-W-0.50', 'STAT-4060-W-0.50', 'STAT-4150-F,W-0.50', 'STAT-4340-W-0.50', 'STAT-4600-F,W-1.00', 'SART-2300-F,W-0.50', 'SART-2610-F,W-0.50', 'SART-2710-W-0.50', 'SART-1060-F,W-0.50', 'SART-2090-F,W-0.50', 'SART-2200-F,W-0.50', 'SART-2800-F,W-0.50', 'SART-3090-F,W-0.50', 'SART-3200-F,W-0.50', 'SART-3300-F,W-0.50', 'SART-3600-W-0.50', 'SART-3660-F,W-0.50', 'SART-3750-F,W-0.50', 'SART-3770-F,W-0.50', 'SART-3800-S,F,W-0.50', 'SART-3900-S,F,W-0.50', 'SART-4130-W-1.00', 'SART-4240-W-1.00', 'SART-4250-W-0.50', 'SART-4260-W-0.50', 'SART-4300-F,W-0.50', 'SART-4330-F,W-1.00', 'SART-4470-W-1.00', 'SART-4720-W-1.00', 'SART-4760-W-1.00', 'SART-4800-W-0.50', 'SART-4810-W-0.50', 'SART-4870-W-0.50', 'SART-4880-W-1.00', 'SART-4890-W-1.00', 'THST-2270-W-0.50', 'THST-2450-W-0.50', 'THST-2500-W-0.50', 'THST-3000-S,F,W-0.50', 'THST-3010-S,F,W-0.50', 'THST-3140-W-0.50', 'THST-3600-F,W-0.50', 'THST-1190-W-0.50', 'THST-1270-W-0.50', 'THST-2050-W-0.50', 'THST-3500-W-0.50', 'THST-4280-W-1.00', 'THST-4290-W-0.50', 'THST-4500-W-1.00', 'TOX-4900-S,F,W-1.00', 'TOX-4910-S,F,W-1.00', 'TOX-3360-S,W-0.50', 'TOX-4100-W-0.50', 'TOX-4200-W-0.50', 'WMST-2000-W-0.50', 'ZOO-3630-W-0.25', 'ZOO-2700-W-0.50', 'ZOO-3050-W-0.50', 'ZOO-3620-W-0.50', 'ZOO-4170-W-0.50', 'ZOO-4330-W-0.50', 'ZOO-4570-W-0.50', 'ZOO-4940-W-0.25', 'ZOO-4950-W-0.25']
        self.assertEqual(matches, notCurrent)

if __name__ == '__main__':
    unittest.main()
