from src.ParseText import parser
from src.WebCourse import WebCourse

import os

from unittest.mock import patch
from unittest import TestCase

class ParseTextTest(TestCase):

    def test_course_valid_1(self):
        course1 = WebCourse("0.50","Topics in Toxicology","TOX","TOX*4200","Open","R. Manderville","12/50")
        self.assertTrue(course1)

    def test_course_valid_2(self):
        course1 = WebCourse("0.75","User Interface Design","CIS","CIS*2170","Closed","D. Flatla","0/40")
        self.assertTrue(course1)

    def test_course_to_string_1(self):
        course1 = WebCourse("0.50","Topics in Toxicology","TOX","TOX*4200","Open","R. Manderville","12/50")
        course1String = str(course1)
        testString1 = "Course Title: Topics in Toxicology\nCourse Code: TOX*4200\nCourse Weight: 0.50\nDepartment: TOX\nStatus: Open\nFaculty: R. Manderville\nCapacity: 12/50\n"
        self.assertEqual(course1String, testString1)

    def test_course_to_string_valid(self):
        course1 = WebCourse("0.50","Topics in Toxicology","TOX","TOX*4200","Open","R. Manderville","12/50")
        course1String = str(course1)
        self.assertTrue(course1)

    def test_hash_1(self):
        course1 = WebCourse("0.50","Topics in Toxicology","TOX","TOX*4200","Open","R. Manderville","12/50")
        testHash1 = "TOX-4200"
        self.assertEqual(testHash1, course1.to_hash())

    def test_hash_2(self):
        course1 = WebCourse("0.75","User Interface Design","CIS","CIS*2170","Closed","D. Flatla","0/40")
        testHash1 = "CIS-2170"
        self.assertEqual(testHash1, course1.to_hash())

if __name__ == '__main__':
    unittest.main()
