from .ParseText import parser
from .WebScrape import scraper
from .Search import Search

import os
import json
import csv

class ParseFactory:
    def __init__(self, ui, scraper_filename):
        self.ui = ui
        self.textData = parser(ui.filename)
        self.webData = scraper(scraper_filename)
        self.__link_datasets()

    # post: adds webkey to course object and coursekey to webcourse object
    def __link_datasets(self):
        for courseKey in self.textData:
            keyValue = courseKey.split("-")
            currentWebKey = keyValue[0] + "-" + keyValue[1]
            try:
                self.textData[courseKey].webKey = currentWebKey
                self.webData[currentWebKey].courseKey = self.textData[courseKey].to_hash()
            except KeyError:
                self.textData[courseKey].webKey = None

    def to_json(self, courseKeyList):
        courseArr = []
        for key in courseKeyList:
            currentCourse = self.textData[key]
            courseArr.append(currentCourse.to_dict(self.webData))
        
        return json.dumps({'courses': courseArr})

    def to_dict(self, courseKeyList):
        courseDict = {}
        for key in courseKeyList:
            courseDict[key] = self.textData[key]

        return courseDict


    def csv_to_dicts(self, fileName):
        dataDir = os.path.dirname(os.getcwd()) + '/backend/export/'
        filePath = dataDir + fileName
        dicts_from_csv = []

        try:
            with open(filePath, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    dicts_from_csv.append(row)

                return dicts_from_csv

        except IOError:
            return None


