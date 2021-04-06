from .UserInterface import UserInterface
from .PickleToFile import PickleToFile

# search functionality:
#   1. Get term to search for in keys
#   2. Search through list of keys for that term (weight, department, code, semester, level)
#   3. Search hash table for each individual key returned from above ^^

class Search:
    # Takes in the list of keys, and the specific search term type and search term for this search
    def __init__(self, userInterface, keys, webCourses):
        self.userInterface = userInterface
        self.keys = keys
        self.termType = None
        self.term = None
        self.webCourses = webCourses

    # Pre: Search was run in UI
    # Post: A list of all keys matching search is returned
    def findKeys(self, params=[None, None]):
        self.termType, self.term = self.userInterface.query(params)

        # break down what we're searching for
        if self.termType == 'weight':
            keys = self.__search(3)
        elif self.termType == 'department':
            keys = self.__search(0)
        elif self.termType == 'code':
            keys = self.__search(1)
        elif self.termType == 'semester':
            keys = self.__search(2)
        elif self.termType == 'level':
            keys = self.__search(4)
        elif self.termType == 'full course code':
            keys = self.__search_full_course_code()
        elif self.termType == 'availability':
            keys = self.__search_availability()
        elif self.termType == 'faculty':
            keys = self.__search_faculty()
        elif self.termType == 'dropped':
            keys = self.__dropped()
        elif self.termType == 'Not in current semester':
            keys = self.__not_in_current()
        elif self.termType == 'capacity_maximum':
            keys = self.__search_by_capacity()
        elif self.termType == 'capacity_minimum':
            keys = self.__search_by_capacity()
        elif self.termType == 'quit':
            keys = 'quit'
        else:
            keys = []

        return keys



    # Pre: the search being run provides us with search term and section of the key to look in
    # Post: A list of all keys matching the search term and search section is returned
    def __search(self, section):
        matchingKeys = []

        if section < 4:
            for key in self.keys:
                splitKey = key.split('-')
                if section == 2:
                    semesterNotInKey = False
                    semester = self.term.split(',')

                    for sem in semester:
                        if sem not in splitKey[section]:
                            semesterNotInKey = True
                            break

                    if semesterNotInKey == False:
                        matchingKeys.append(key)

                elif splitKey[section] == self.term:
                    matchingKeys.append(key)

        elif section == 4:
            # Search by course level
            for key in self.keys:
                splitKey = key.split('-')
                termString = str(self.term)
                # After ASCI*4710, an empty course code appears. This accounts for that
                # Fix the search
                if splitKey[1] != "":
                    if splitKey[1][0] == termString[0]:
                        matchingKeys.append(key)

        return matchingKeys

    # Pre: the search being run provides us with search term and section of the key to look in
    # Post: A list of all keys matching the search term and search section is returned
    def __search_full_course_code(self):
        matchingKeys = []

        # Obtain the Department and Course Code from search term
        query = self.term.split('*')

        for key in self.keys:
            splitKey = key.split('-')
            if splitKey[0].lower() == query[0].lower() and splitKey[1] == query[1]:
                matchingKeys.append(key)

        return matchingKeys

    # Pre: The search being run provides us with the status of the course to look for
    # Post: A list of all keys matching the status of the course is returned
    def __search_availability(self):
        matchingKeys = []

        # iterate through courses looking for open, closed, or all courses,
        # storing the associated course key
        for key, course in self.webCourses.items():
            if course.get_status().lower() == self.term or self.term == 'all':
                if course.courseKey != None: # get rid of graduate courses
                    matchingKeys.append(course.courseKey)

        return matchingKeys

    # Pre: The search being run provides us with the Name of the Faculty member to look for
    # Post: A list of all keys matching the Faculty member name
    def __search_faculty(self):
        matchingKeys = []

        # iterate through courses looking for matching faculty members name,
        # storing the associated course key
        for key, course in self.webCourses.items():
            if self.term.lower() in course.get_faculty().lower() or course.get_faculty().lower() in self.term.lower():
                if course.courseKey != None: # get rid of graduate courses
                    matchingKeys.append(course.courseKey)

        return matchingKeys

    # Pre: The search being run provides us with a list of courses that have students drop
    # Post: A list of all keys with changed capacity is returned
    def __dropped(self):
        matchingKeys = []
        pickle = PickleToFile("data/saved-webscrape.txt")
        oldHash = pickle.retrievePickledObject()

        # iterate through courses and compairing them to the old hash to see if capacity has changed,
        for key, course in self.webCourses.items():
            if course.capacity != oldHash[key].capacity:
                if course.courseKey != None: # get rid of graduate courses
                    matchingKeys.append(course.courseKey)

        #Updating pickle file
        print("\nUpdating list of saved course capacities\n")
        pickle.pickleObjectToFile(self.webCourses)
        return matchingKeys

    # Pre: The search being run provides us with a list of courses that should be offered in the winter but currently arn't
    # Post: A off all keys that are offered in the current semester
    def __not_in_current(self):
        matchingKeys = []

        # We don't have access to the full hash table in here so gathering all winter keys and checking them in main
        for key in self.keys:
            splitKey = key.split('-')
            if "W" in splitKey[2]:
                matchingKeys.append(key)

        return matchingKeys

    # Pre: The search being run provides us with the capacity of the course to look for
    # Post: A list of all keys matching the capacity requirement of the course is returned
    def __search_by_capacity(self):
        matchingKeys = []

        if self.termType == 'capacity_maximum':
            # iterate through courses looking for matching capacity type
            # storing the associated course key
            for key, course in self.webCourses.items():
                if course.get_capacity() < int(self.term):
                    if course.courseKey != None: # get rid of graduate courses
                        matchingKeys.append(course.courseKey)

        elif self.termType == 'capacity_minimum':
            # iterate through courses looking for matching capacity type
            # storing the associated course key
            for key, course in self.webCourses.items():
                if course.get_capacity() >= int(self.term):
                    if course.courseKey != None: # get rid of graduate courses
                        matchingKeys.append(course.courseKey)

        return matchingKeys
