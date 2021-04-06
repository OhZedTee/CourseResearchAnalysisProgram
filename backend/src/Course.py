import json

class Course:
    def __init__(self,semesters,weight,title,department,coursecode,description,restrictions,prereqs):
        self.semesters = semesters
        self.weight = weight
        self.title = title
        self.department = department
        self.coursecode = coursecode
        self.description = description
        self.restrictions = restrictions
        self.prereqs = prereqs
        self.webKey = None

    def __str__(self):
        return("Course Title: " + self.title + "\nCourse Code: " + self.coursecode + "\nSemesters Offered: " + self.semesters + "\nCourse Weight: " + self.weight + "\nDepartment: " + self.department + "\nDescription: " + self.description + "\nRestrictions: " +  self.restrictions + "\nPrerequisites: " + self.prereqs)

    #Course code on the txt file is formatted ex: CIS*2750
    def to_hash(self):
        keyValues = self.coursecode.replace(',', '').split("*")
        text = keyValues[0] + "-" + keyValues[1] + "-" + self.semesters + "-" + self.weight
        return text

    #Convert Course Data to dict
    def to_dict(self, webData):

        courseData = {}
        courseData['semesters'] = self.semesters
        courseData['weight'] = self.weight
        courseData['title'] = self.title
        courseData['department'] = self.department
        courseData['coursecode'] = self.coursecode
        courseData['description'] = self.description
        courseData['restrictions'] = self.restrictions
        courseData['prereqs'] = self.prereqs 
        courseData['status'] = 'Not Available Winter (NAW)'

        if (self.webKey != None):
            courseData['status'] =  webData[self.webKey].get_status()
            courseData['availability'] =  webData[self.webKey].get_availability()
            courseData['capacity'] =  webData[self.webKey].get_capacity()
            courseData['faculty'] =  webData[self.webKey].get_faculty()

        return courseData


    @staticmethod
    def Find(coursecode, courses_dict):
        for _, course in courses_dict.items():
            if course.coursecode.replace(',', '') == coursecode.replace('-', '*'):
                return course
        return None