from src import UserInterface

from unittest.mock import patch
from unittest import TestCase
from io import StringIO

@patch('src.UserInterface.get_input', return_value='course-descriptions.txt')
def setup_ui(self, input):
    return UserInterface.UserInterface()


class UserIntefaceTest(TestCase):

    @patch('src.UserInterface.get_input', return_value='course-descriptions.txt')
    def test_greet_and_fetch_data(self, input):
        ui = UserInterface.UserInterface()
        self.assertEqual(ui.filename.split('/')[-1], 'course-descriptions.txt')



    @patch('src.UserInterface.get_input', return_value='1')
    def test_query_course_weight(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'weight')
        self.assertEqual(result[1], '0.25')

    @patch('src.UserInterface.get_input', return_value='2')
    def test_query_department(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'department')
        self.assertEqual(result[1], 'AGR')

    @patch('src.UserInterface.get_input', return_value='3')
    def test_query_course_code(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'code')
        self.assertEqual(result[1], '3')


    @patch('src.UserInterface.get_input', return_value='4')
    def test_query_semester(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'semester')
        self.assertEqual(result[1], 'F,W')

    @patch('src.UserInterface.get_input', return_value='5')
    def test_query_level(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'level')
        self.assertEqual(result[1], 5)

    @patch('src.UserInterface.get_input', return_value='2')
    def test_multisearch_filter_success(self, input):
        ui = setup_ui(input)
        result, type_multi = ui.multisearch()
        self.assertTrue(result)
        self.assertEqual(type_multi, 'filter')

    @patch('src.UserInterface.get_input', return_value='3')
    def test_multisearch_filter_success(self, input):
        ui = setup_ui(input)
        result, type_multi = ui.multisearch()
        self.assertTrue(result)
        self.assertEqual(type_multi, 'combine')

    @patch('src.UserInterface.get_input', return_value='1')
    def test_multisearch_failure(self, input):
        ui = setup_ui(input)
        result, type_multi = ui.multisearch()
        self.assertFalse(result)
        self.assertEqual(type_multi, 'no')

    @patch('src.UserInterface.get_input', side_effect=['2', 'Summary'])
    def test_export_all(self, input):
        ui = setup_ui(input)
        result = ui.export()
        self.assertEqual(result[0], 'all')
        self.assertEqual(result[1], 'Summary')

    @patch('src.UserInterface.get_input', side_effect=['3', 'SearchSpecific'])
    def test_export_search(self, input):
        ui = setup_ui(input)
        result = ui.export()
        self.assertEqual(result[0], 'search')
        self.assertEqual(result[1], 'SearchSpecific')

    @patch('src.UserInterface.get_input', side_effect=['3', 'Search Test', 'Search-Test.txt'])
    def test_export_filename(self, input):
        ui = setup_ui(input)
        result = ui.export()
        self.assertEqual(result[0], 'search')
        self.assertEqual(result[1], 'Search-Test')

    @patch('src.UserInterface.get_input', side_effect=['7', '1'])
    def test_availability(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'availability')
        self.assertEqual(result[1], 'open')

    @patch('src.UserInterface.get_input', return_value='11')
    def test_capacity_maximum(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'capacity_maximum')
        self.assertEqual(result[1], 11)

    @patch('src.UserInterface.get_input', return_value='12')
    def test_capacity_minimum(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'capacity_minimum')
        self.assertEqual(result[1], 12)

    @patch('src.UserInterface.get_input', side_effect=["8", "D. Flatla"])
    def test_faculty(self, input):
        ui = setup_ui(input)
        result = ui.query()
        self.assertEqual(result[0], 'faculty')
        self.assertEqual(result[1], 'D. Flatla')
        
    def test_output_query(self):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            ui = setup_ui(None)
            format_string = "Course Name: CIS*4250\nCourse Weight: 0.5\nDepartment: CIS\nSemester: F,W\nLevel: 4\nCode: 4520"
            ui.output_query(format_string)
            self.assertIn(format_string, fakeOutput.getvalue().strip())


if __name__ == '__main__':
    unittest.main()