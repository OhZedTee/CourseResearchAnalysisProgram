import os

def get_input(text, param=None):
        if param != None:
            return param

        return input(str(text))

class UserInterface:
    """Base Class for all input and output to the user"""

    def __init__(self, fileName = None):
        self._filename = None
        self._greeting = ("\n-------------------------------------------------------------------------------------------------------------\n"
                          "Welcome to the University of Guelph Course Research and Analysis Program, CRAP for short.\n\nTo get started, "
                          "we need you to provide the filename to the dataset in the main directory\nFor more information, please visit\n\n\n"
                          "https://git.socs.uoguelph.ca/team2-design5/project/-/wikis/Data-Set-Generation\n"
                          "-------------------------------------------------------------------------------------------------------------")
        self.__greet_and_fetch_data(fileName)

    @property
    def filename(self):
        """Get Filename of the dataset"""
        return self._filename

    @filename.setter
    def filename(self, name):
        """Set Filename of the dataset"""
        self._filename = name


    # Pre: N/A
    # Post: Stores filename in filename attribute
    def __greet_and_fetch_data(self, fileName):
        """Outputs greeting and retrieves filename from user"""
        print(self._greeting)
        while 1:
            data_dir = os.getcwd()
            if fileName == None:
                fileName = get_input("Dataset filename: ")

            self._filename = data_dir + "/data/" + fileName
            try:
                with open(self._filename, 'r'):
                    print("Thank you, just a moment...")
                    break
            except:
                print("Invalid file name: " + self._filename + ", please try again.")

    # Pre: Query method was run, and query value is needed
    # Post: Returns Course Weight
    def __search_course_weight(self, param=None):
        """Gets course weight choice from user"""
        if param != None:
            return param

        while(1):
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "Okay, Would you like to find courses with a weight of:\n\n"
                    "1. 0.25\n2. 0.5\n3. 0.75\n4. 1\n"
                    "-------------------------------------------------------------------------------------------------------------"))
                query_choice = int(get_input("Please enter a number between 1 and 4: "))

                switch = {
                    1 : "0.25",
                    2 : "0.50",
                    3 : "0.75",
                    4 : "1.00"
                }

                # Raise value error if not an integer from 1 - 5
                query_value = switch.get(query_choice, "None")
                if query_value == "None":
                    raise ValueError

                return query_value
            except ValueError:
                print("This is not a valid query type. Please provide a number between 1 and 4.")

    # Pre: Query method was run, and query value is needed
    # Post: Returns Department code
    def __search_department(self, param=None):
        """Gets department choice from user"""
        if param != None:
            return param

        while(1):
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "Okay, Which Department would you like to find courses from?\n\n"
                    "1. Accounting\n"
                    "2. Agriculture\n"
                    "3. Anatomy\n"
                    "4. Animal Science\n"
                    "5. Anthropology\n"
                    "6. Arabic\n"
                    "7. Art History\n"
                    "8. Arts and Sciences\n"
                    "9. Biochemistry\n"
                    "10. Biology\n"
                    "11. Biomedical Sciences\n"
                    "12. Botany\n"
                    "13. Business\n"
                    "14. Chemistry\n"
                    "15. Chinese\n"
                    "16. Classical Studies\n"
                    "17. Computing and Information Science\n"
                    "18. Co-operative Education\n"
                    "19. Crop Science\n"
                    "20. Culture and Technology\n"
                    "21. Economics\n"
                    "22. Environmental Design and Rural Development\n"
                    "23. Engineering\n"
                    "24. English\n"
                    "25. Environmental Management\n"
                    "26. Environmental Sciences\n"
                    "27. Equine\n"
                    "28. European Studies\n"
                    "29. External Courses\n"
                    "30. Finance\n"
                    "31. Family Relations and Human Development\n"
                    "32. Food, Agricultural and Resource Economics\n"
                    "33. Food Science\n"
                    "34. French Studies\n"
                    "35. Geography\n"
                    "36. German Studies\n"
                    "37. Greek\n"
                    "38. History\n"
                    "39. Horticultural Science\n"
                    "40. Hospitality and Tourism Management\n"
                    "41. Human Resources and Organizational Behaviour\n"
                    "42. Human Kinetics\n"
                    "43. Humanities\n"
                    "44. Indigenous Studies\n"
                    "45. Interdisciplinary Physical Science\n"
                    "46. Interdisciplinary Social Science\n"
                    "47. Interdisciplinary University\n"
                    "48. Integrative Biology\n"
                    "49. International Development\n"
                    "50. Italian Studies\n"
                    "51. Landscape Architecture\n"
                    "52. Latin\n"
                    "53. Linguistics\n"
                    "54. Management\n"
                    "55. Marketing and Consumer Studies\n"
                    "56. Mathematics\n"
                    "57. Microbiology \n"
                    "58. Molecular and Cellular Biology\n"
                    "59. Molecular Biology and Genetics\n"
                    "61. Nanoscience\n"
                    "60. Music\n"
                    "62. Neuroscience\n"
                    "63. Nutrition\n"
                    "64. Organic Agriculture\n"
                    "65. One Health\n"
                    "66. Pathology\n"
                    "67. Pharmacology\n"
                    "68. Philosophy\n"
                    "69. Physics\n"
                    "70. Physiology\n"
                    "71. Plant Biology\n"
                    "72. Political Science\n"
                    "73. Population Medicine\n"
                    "74. Portuguese\n"
                    "75. Psychology\n"
                    "76. Real Estate and Housing\n"
                    "77. Sociology\n"
                    "78. Sociology and Anthropology\n"
                    "79. Spanish\n"
                    "80. Statistics\n"
                    "81. Studio Art\n"
                    "82. Theatre Studies\n"
                    "83. Toxicology\n"
                    "84. Veterinary Medicine\n"
                    "85. Women's Studies\n"
                    "86. Zoology\n"
                        "-------------------------------------------------------------------------------------------------------------"))

                query_choice = int(get_input("Please enter a number between 1 and 86: "))

                switch = {
                    1 : "ACCT",
                    2 : "AGR",
                    3 : "BIOM",
                    4 : "ANSC",
                    5 : "ANTH",
                    6 : "ARAB",
                    7 : "ARTH",
                    8 : "ASCI",
                    9 : "BIOC",
                    10 : "BIOL",
                    11 : "BIOM",
                    12 : "BOT",
                    13 : "BUS",
                    14 : "CHEM",
                    15 : "CHIN",
                    16 : "CLAS",
                    17 : "CIS",
                    18 : "COOP",
                    19 : "CROP",
                    20 : "CTS",
                    21 : "ECON",
                    22 : "EDRD",
                    23 : "ENGG",
                    24 : "ENGL",
                    25 : "ENVM",
                    26 : "ENVS",
                    27 : "EQN",
                    28 : "EURO",
                    29 : "XSEN",
                    30 : "FIN",
                    31 : "FRHD",
                    32 : "FARE",
                    33 : "FOOD",
                    34 : "FREN",
                    35 : "GEOG",
                    36 : "GERM",
                    37 : "GREK",
                    38 : "HIST",
                    39 : "HORT",
                    40 : "HTM",
                    41 : "HROB",
                    42 : "HK",
                    43 : "HUMN",
                    44 : "INDG",
                    45 : "IPS",
                    46 : "ISS",
                    47 : "UNIV",
                    48 : "IBIO",
                    49 : "IDEV",
                    50 : "ITAL",
                    51 : "LARC",
                    52 : "LAT",
                    53 : "LING",
                    54 : "MGMT",
                    55 : "MCS",
                    56 : "MATH",
                    57 : "MICR",
                    58 : "MCB",
                    59 : "MBG",
                    60 : "MUSC",
                    61 : "NANO",
                    62 : "NEUR",
                    63 : "NUTR",
                    64 : "OAGR",
                    65 : "ONEH",
                    66 : "PATH",
                    67 : "BIOM",
                    68 : "PHIL",
                    69 : "PHYS",
                    70 : "BIOM",
                    71 : "PBIO",
                    72 : "POLS",
                    73 : "POPM",
                    74 : "PORT",
                    75 : "PSYC",
                    76 : "REAL",
                    77 : "SOC",
                    78 : "SOAN",
                    79 : "SPAN",
                    80 : "STAT",
                    81 : "SART",
                    82 : "THST",
                    83 : "TOX",
                    84 : "VETM",
                    85 : "WMST",
                    86 : "ZOO",
                }

                # Raise value error if not an integer from 1 - 86
                query_value = switch.get(query_choice, "None")
                if query_value == "None":
                    raise ValueError

                return query_value
            except ValueError:
                print("This is not a valid query type. Please provide a number between 1 and 86.")

    # Pre: Query method was run, and query value is needed
    # Post: Returns Course Code
    def __search_course_code(self, param=None):
        """Gets course code from user"""
        if param != None:
            return param
            
        while(1):
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "Okay, please enter a course code\n"
                    "-------------------------------------------------------------------------------------------------------------"))
                return str(int(get_input("Course Code: ")))
            except ValueError:
                print(("This is not a valid Course Code, please provide just the course number."
                       "\n(e.g. if you're looking for CIS1500, enter 1500)"))

    # Pre: Query method was run, and query value is needed
    # Post: Returns Semester
    def __search_semester(self, param=None):
        """Gets semester choice from user"""
        if param != None:
            return param
            
        while(1):
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "Okay, Would you like to find courses available in the:\n\n"
                    "1. Fall\n2. Winter\n3. Summer\n4. Fall and Winter\n5. Fall and Summer\n6. Winter and Summer\n7. Fall, Winter, and Summer\n"
                    "-------------------------------------------------------------------------------------------------------------"))
                query_choice = int(get_input("Please enter a number between 1 and 7: "))

                switch = {
                    1 : "F",
                    2 : "W",
                    3 : "S",
                    4 : "F,W",
                    5 : "F,S",
                    6 : "W,S",
                    7 : "F,W,S"
                }

                # Raise value error if not an integer from 1 - 5
                query_value = switch.get(query_choice, "None")
                if query_value == "None":
                    raise ValueError

                return query_value
            except ValueError:
                print("This is not a valid query type. Please provide a number between 1 and 7.")


    # Pre: Query method was run, and query value is needed
    # Post: Returns Course Level
    def __search_level(self, param=None):
        """Gets course level choice from user"""
        if param != None:
            return param
            
        while (1):
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                       "Okay, Which level would you like to find courses in:\n\n"
                       "1. 1000\n2. 2000\n3. 3000\n4. 4000\n5. 5000\n"
                       "-------------------------------------------------------------------------------------------------------------"))
                query_value = int(get_input("Please enter a number between 1 and 5: "))


                # Raise value error if not an integer from 1 - 5
                if query_value > 5:
                    raise ValueError

                return query_value
            except ValueError:
                print("This is not a valid query type. Please provide a number between 1 and 5.")

    # Pre: Query method was run and query value is needed
    # Post: Returns Full Course Code
    def __search_full_course_code(self, param=None):
        '''Gets course code from user'''
        if param != None:
            return param
        
        while(1):
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                       "Okay, please enter a full course code (e.g. CIS*1500)\n"
                       "-------------------------------------------------------------------------------------------------------------"))

                query_value = str(get_input("Course Code: "))
                if query_value.find("*") == -1:
                    raise ValueError

                return query_value
            except ValueError:
                print(("This is not a valid Course Code, please include an asterisk in your search query"
                       "\n(e.g. if you're looking for CIS1500, enter CIS*1500)"))

    # Pre: Query method was run and query value is needed
    # Post: Returns option from user to filter out full courses or not
    def __search_availability(self, param=None):
        '''Get Course Availability choice from user'''
        if param != None:
            return param
        
        while 1:
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "How would you like to filter your search? \n\n"
                    "1. Give me only for courses that are open for registration \n2. Give me only courses that are full\n3. Give me courses with either form of availability"
                    "\n-------------------------------------------------------------------------------------------------------------"))

                query_choice = int(get_input("Please enter a number between 1 and 3: "))

                switch = {
                    1 : 'open',
                    2 : 'closed',
                    3 : 'all'
                }

                query_value = switch.get(query_choice, "None")
                if query_value == "None":
                    raise ValueError

                return query_value

            except ValueError:
                print("This is not a valid Course Availability option. Please provide a number between 1 and 3.")

    # Pre: Query method was run and query value is needed
    # Post: Returns a Faculty Member name for searching
    def __search_faculty(self, param=None):
        if param != None:
            return param
        
        print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
               "Okay, please enter a faculty members name (e.g. D. Flatla)\n"
               "-------------------------------------------------------------------------------------------------------------"))
        query_value = str(get_input("Faculty Name: "))
        return query_value

    def __quit_loop(self):
        print("Thank you for using our services. Have a great day!")
        return 'quit'

    def __dropped(self):
        print("\n\nNow checking which courses had students drop since the last time you've checked")
        return ""

    def __not_in_current(self):
        return ""

    def __capacity(self, param=None):
        """Gets course capacity from user"""
        if param != None:
            return param
        
        while(1):
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "Okay, please enter a Max/Min Capacity\n"
                    "-------------------------------------------------------------------------------------------------------------"))
                return int(get_input("Capacity: "))
            except ValueError:
                print("This is not a valid Capacity, please provide a number.")


    # Pre: Dataset is parsed and queries are ready to be made
    # Post: Query type and value is returned as a tuple
    def query(self, params=[None, None]):
        """Gets query type and input from user"""
        try:
            print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "Let's make a query! Would you like to: \n\n"
                    " 1. Search by Course Weight\n"
                    " 2. Search by Department\n"
                    " 3. Search by Course Code\n"
                    " 4. Search by Semester\n"
                    " 5. Search by Course Level\n"
                    " 6. Search by Full Course Code (e.g. CIS*1500)\n"
                    " 7. Search by Availability\n"
                    " 8. Search by Faculty\n"
                    " 9. Check dropped courses\n"
                    "10. Check current semester courses not being offered\n"
                    "11. Search by Capacity Maximum\n"
                    "12. Search by Capacity Minimum\n"
                    "13. Quit\n"
                    "-------------------------------------------------------------------------------------------------------------"))

            query_choice = int(get_input("Please enter a number between 1 and 13: ", params[0]))

            switch = {
                1  : lambda: self.__search_course_weight(params[1]),
                2  : lambda: self.__search_department(params[1]),
                3  : lambda: self.__search_course_code(params[1]),
                4  : lambda: self.__search_semester(params[1]),
                5  : lambda: self.__search_level(params[1]),
                6  : lambda: self.__search_full_course_code(params[1]),
                7  : lambda: self.__search_availability(params[1]),
                8  : lambda: self.__search_faculty(params[1]),
                9  : lambda: self.__dropped(),
                10 : lambda: self.__not_in_current(),
                11 : lambda: self.__capacity(params[1]),
                12 : lambda: self.__capacity(params[1]),
                13 : lambda: self.__quit_loop()
            }

            # Raise value error if not an integer from 1 - 5
            query_func = switch.get(query_choice, "None")
            if query_func == "None":
                raise ValueError

            query_value = query_func()

            switch = {
                1  : 'weight',
                2  : 'department',
                3  : 'code',
                4  : 'semester',
                5  : 'level',
                6  : 'full course code',
                7  : 'availability',
                8  : 'faculty',
                9  : 'dropped',
                10 : 'Not in current semester',
                11 : 'capacity_maximum',
                12 : 'capacity_minimum',
                13 : 'quit'
            }

            return (switch.get(query_choice), query_value)
        except ValueError:
            print("This is not a valid query type. Please provide a number between 1 and 13.")
            self.query()

    # Pre: None
    # Post: Result from user on multisearch request - True, False do we want to search
    def multisearch(self):
        '''Ask the user if they want to perform a multisearch'''
        while 1:
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                       "Would you like to filter or combine your search with more parameters?\n\n"
                       "1. No \n2. Yes, filter my search\n3. Yes, combine my search"
                       "\n-------------------------------------------------------------------------------------------------------------"))

                choice = int(get_input("Please enter a number between 1 and 3: "))

                switch = {
                    1 : 'no',
                    2 : 'filter',
                    3 : 'combine'
                }

                input_val = switch.get(choice, "None")
                if input_val == "None":
                    raise ValueError

                option = False if input_val == 'no' else True

                return option, input_val

            except ValueError:
                print("This is not a valid multi search option. Please provide a number between 1 and 3.")


    # Pre: User wants to export data
    # Post: User picks export or not, if so gets filename and returns export type and filename
    def export(self):
        '''Ask the user if they want to export results'''
        while 1:
            try:
                print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "Would you like to export course data: \n\n"
                    "1. No \n2. Yes, all course data\n3. Yes, all course data that matched my search "
                    "\n-------------------------------------------------------------------------------------------------------------"))

                choice = int(get_input("Please enter a number between 1 and 3: "))

                switch = {
                    1 : 'no',
                    2 : 'all',
                    3 : 'search'
                }

                input_val = switch.get(choice, "None")
                if input_val == "None":
                    raise ValueError

                filename = ''
                if input_val != 'no':
                    filename = self.__get_file_name()

                return input_val, filename

            except ValueError:
                print("This is not a valid export option. Please provide a number between 1 and 3.")



    # Pre: Export in progress, requires file name
    # Post: File name returned from user without file extension
    def __get_file_name(self):
        '''Gets file name from user and removes any file extensions. Verifies file name is one word'''
        filename = ''

        while 1:
            print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "In order to export the data file, we need a unique identifier. For example, 'Summary', or 'Course_Code'.\n"
                    "Please provide only one word!"
                    "\n-------------------------------------------------------------------------------------------------------------"))
            filename = get_input('Export File Identifier: ')

            # make sure the filename provided is one word and remove any potential file extensions
            if len(filename.split()) == 1:
                filename = filename.split('.')[0]
                break

        return filename



    # Pre: Expecting result to be a formatted string that is prepared for user output
    # Post: Result is outputted to the user
    def output_query(self, result):
        '''Print result to the user'''
        print(("\n\n-------------------------------------------------------------------------------------------------------------\n"
                    "Your query resulted in the following:\n\n") + result +
                    ("\n-------------------------------------------------------------------------------------------------------------"))
