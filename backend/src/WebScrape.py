#import requests
from bs4 import BeautifulSoup
import os
import sys
import re
from datetime import date

from .WebCourse import WebCourse


def scraper(filename):

    # Initialize the hash table
    hashTableOfCourses = {}

    with open(filename, encoding="utf8") as f:
        print("Reading Webadvisor data, this will take a while...")

        # Read in the webadvisor data
        data = f.read()
        soup = BeautifulSoup(data, 'html.parser')

        print("Scraping WebAdvisor data, this shouldn't take long...")

        # Get all the text without HTML tags so we can parse it
        lines = soup.get_text()
        linesSplit = lines.split("\n")

        # Set flags for parsing
        courseCodeFlag = False
        courseTitleFlag = False
        courseDepartmentFlag = False
        courseFacultyFlag = False
        courseCapacityFlag = False
        courseWeightFlag = False
        courseStatusFlag = False

        # Set strings for parsing
        courseCode = ""
        courseTitle = ""
        courseDepartment = ""
        courseFaculty = ""
        courseCapacity = ""
        courseWeight = ""
        courseStatus = ""

        # Parse through each line of WebAdvisor data, using beautiful soup to convert it all to text
        for line in linesSplit:
            # if the line is just a new line, this check skips it
            if line:

                #Check Course status
                if courseStatusFlag == False:
                    if line == "Open" or line == "Closed":
                        
                        courseStatus = line
                        courseStatusFlag = True

                # Check for Course code
                if courseCodeFlag == False:
                    if re.match("^[A-Z]{2,4}\*\d{4}", line):

                        courseInfoSplit = line.split("*")

                        # Get department and course code
                        courseDepartment = courseInfoSplit[0]
                        courseCode = courseInfoSplit[0] + "*" + courseInfoSplit[1]

                        # Get the title
                        courseTitleSplit = courseInfoSplit[2].split(")")
                        courseTitle = courseTitleSplit[1]

                        # Set the flags to know we have this information
                        courseDepartmentFlag = True
                        courseCodeFlag = True
                        courseTitleFlag = True

                # Check for faculty
                if courseFacultyFlag == False:
                    if re.match("^[A-Z]\.[ ][A-Z][a-z]*.*", line) or line == "TBA  TBA":
                        
                        # Set course faculty
                        courseFaculty = line
                        courseFacultyFlag = True
                
                # Check for capacity
                if courseCapacityFlag == False:
                    if re.match("^[0-9]*[ ]\/[ ][0-9]*", line):

                        #Set course capacity
                        courseCapacity = line
                        courseCapacityFlag = True

                # Check for course weight
                if courseWeightFlag == False:
                    if re.match("^[0-9]*\.[0-9]{1,2}", line):

                        # Set course weight
                        courseWeight = line
                        courseWeightFlag = True

                # Deal with the special case of MGMT*4050, which has no apparent capacity and is just a new line in the capacity section.
                if courseCode == "MGMT*4050":
                    courseCapacity = "0 / 0"
                    courseCapacityFlag = True

                # Check if all the flags have been set, if so we can add a course object with the values to the hash table
                if courseCodeFlag == True and courseDepartmentFlag == True and courseFacultyFlag == True and courseStatusFlag == True and courseTitleFlag == True and courseCapacityFlag == True and courseWeightFlag == True:

                    # Generate web course code object
                    courseToAdd = WebCourse(courseWeight, courseTitle, courseDepartment, courseCode, courseStatus, courseFaculty, courseCapacity)

                    # Check the hash table if this key is already in it
                    if courseToAdd.to_hash() not in hashTableOfCourses.keys():
                        hashTableOfCourses[courseToAdd.to_hash()] = courseToAdd
                    else:
                        # Update the course with new capacity level
                        originalCourseObject = hashTableOfCourses.get(courseToAdd.to_hash())
                        originalCapacity = originalCourseObject.capacity
                        capacityToAdd = courseToAdd.capacity

                        # Determine the new numerator and denominator for capacity
                        capacityToAddSplit = capacityToAdd.split("/")
                        originalCapacitySplit = originalCapacity.split("/")
                        # Deal with MGMT*4050 which doesn't have availability information
                        if capacityToAddSplit[0] == "\n":
                            newAvailableCapacity = 0
                            newTotalCapacity = 0
                        else:
                            newAvailableCapacity = int(capacityToAddSplit[0]) + int(originalCapacitySplit[0])
                            newTotalCapacity = int(capacityToAddSplit[1]) + int(originalCapacitySplit[1])

                        # Update status
                        if newAvailableCapacity > 0:
                            originalCourseObject.status = "Open"

                        # Add the new values to the old values
                        newCapacity = str(newAvailableCapacity) + " / " + str(newTotalCapacity)

                        # Update the object
                        originalCourseObject.capacity = newCapacity

                        # Reintegrate the updated object into the hash table
                        hashTableOfCourses[originalCourseObject.to_hash()] = originalCourseObject

                    # Reset all the flags
                    courseCodeFlag = False
                    courseTitleFlag = False
                    courseDepartmentFlag = False
                    courseFacultyFlag = False
                    courseCapacityFlag = False
                    courseWeightFlag = False
                    courseStatusFlag = False

                    # Reset all the strings
                    courseCode = ""
                    courseTitle = ""
                    courseDepartment = ""
                    courseFaculty = ""
                    courseCapacity = ""
                    courseWeight = ""
                    courseStatus = ""
    print('Done scraping!')
    return hashTableOfCourses