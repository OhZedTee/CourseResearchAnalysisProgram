from src.ParseText import parser
from src.Course import Course

import os

from unittest.mock import patch
from unittest import TestCase

class ParseTextTest(TestCase):

    def test_course_valid_1(self):
        course1 = Course("W","0.50","Topics in Toxicology","Department of Biomedical Sciences, School of Environmental Sciences","TOX*4200","Topics in toxicology will consist of oral and written presentations by students, faculty members, and guest lecturers. The emphasis will be on the broad integrative aspects of toxicology with particular reference to the whole organism and higher levels of natural systems; risk assessment and regulatory toxicology.","Restricted to students in BSCH.TOX , BSCH.TOX:C","TOX*2000, (CHEM*3430, TOX*3300)")
        self.assertTrue(course1)

    def test_course_valid_2(self):
        course2 = Course("W","0.50","Migration, Inequality and Social Change","Department of Sociology and Anthropology","SOAN*4260","This seminar critically examines the complex relationships between migration, inequality and social change. Students will develop their understanding of key debates in contemporary migration, exploring relevant theory, research and public policy. Topics may include the migration-development nexus, the role of migration policies in structuring inequalities, migrant rights and resistance, and transnational families.","","12.50 credits including (IDEV*2100 or SOAN*2120), (1 of ANTH*2160 , ANTH*2180, IDEV*2300, IDEV*2500, SOAN*2112, SOC*2080)")
        self.assertTrue(course2)

    def test_course_to_string_1(self):
        course1 = Course("W","0.50","Topics in Toxicology","Department of Biomedical Sciences, School of Environmental Sciences","TOX*4200","Topics in toxicology will consist of oral and written presentations by students, faculty members, and guest lecturers. The emphasis will be on the broad integrative aspects of toxicology with particular reference to the whole organism and higher levels of natural systems; risk assessment and regulatory toxicology.","Restricted to students in BSCH.TOX , BSCH.TOX:C","TOX*2000, (CHEM*3430, TOX*3300)")
        course1String = str(course1)
        testString1 = "Course Title: Topics in Toxicology\nCourse Code: TOX*4200\nSemesters Offered: W\nCourse Weight: 0.50\nDepartment: Department of Biomedical Sciences, School of Environmental Sciences\nDescription: Topics in toxicology will consist of oral and written presentations by students, faculty members, and guest lecturers. The emphasis will be on the broad integrative aspects of toxicology with particular reference to the whole organism and higher levels of natural systems; risk assessment and regulatory toxicology.\nRestrictions: Restricted to students in BSCH.TOX , BSCH.TOX:C\nPrerequisites: TOX*2000, (CHEM*3430, TOX*3300)"
        self.assertEqual(course1String, testString1)

    def test_course_to_string_valid(self):
        course1 = Course("W","0.50","Topics in Toxicology","Department of Biomedical Sciences, School of Environmental Sciences","TOX*4200","Topics in toxicology will consist of oral and written presentations by students, faculty members, and guest lecturers. The emphasis will be on the broad integrative aspects of toxicology with particular reference to the whole organism and higher levels of natural systems; risk assessment and regulatory toxicology.","Restricted to students in BSCH.TOX , BSCH.TOX:C","TOX*2000, (CHEM*3430, TOX*3300)")
        course1String = str(course1)
        self.assertTrue(course1)

    def test_hash_1(self):
        course1 = Course("W","0.50","Topics in Toxicology","Department of Biomedical Sciences, School of Environmental Sciences","TOX*4200","Topics in toxicology will consist of oral and written presentations by students, faculty members, and guest lecturers. The emphasis will be on the broad integrative aspects of toxicology with particular reference to the whole organism and higher levels of natural systems; risk assessment and regulatory toxicology.","Restricted to students in BSCH.TOX , BSCH.TOX:C","TOX*2000, (CHEM*3430, TOX*3300)")
        testHash1 = "TOX-4200-W-0.50"
        self.assertEqual(testHash1, course1.to_hash())

    def test_hash_2(self):
       	course2 = Course("W","0.50","Migration, Inequality and Social Change","Department of Sociology and Anthropology","SOAN*4260","This seminar critically examines the complex relationships between migration, inequality and social change. Students will develop their understanding of key debates in contemporary migration, exploring relevant theory, research and public policy. Topics may include the migration-development nexus, the role of migration policies in structuring inequalities, migrant rights and resistance, and transnational families.","","12.50 credits including (IDEV*2100 or SOAN*2120), (1 of ANTH*2160 , ANTH*2180, IDEV*2300, IDEV*2500, SOAN*2112, SOC*2080)")
        testHash2 = "SOAN-4260-W-0.50"
        self.assertEqual(testHash2, course2.to_hash())

if __name__ == '__main__':
    unittest.main()
