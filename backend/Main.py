import os
import json
import fnmatch

from src.UserInterface import UserInterface
from src.ParseText import parser
from src.Search import Search
from src.Exporter import Exporter
from src.ScrapeCron import scrape_to_HTML
from src.ParseFactory import ParseFactory
from src.PickleToFile import PickleToFile
from src.Course import Course


from flask import Flask, redirect, url_for, request, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
# A bit awkward, but we need this CORS stuff so that we can make requests in local dev environments
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
userInterface = None
factory = None
pickle = None
search = None
multi = None
results = None

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/scrape', methods = ['PATCH'])
def scrape():
    global factory
    global userInterface

    scraper_filename, new_file = scrape_to_HTML()

    # Create course table with parser using dataset
    if factory == None or new_file == True:
        factory = ParseFactory(userInterface, scraper_filename)
        return '', 201, {'Content-Type':'application/json'}

    return '', 204, {'Content-Type':'application/json'}

def init(fileName = None):
    global userInterface
    global factory
    global pickle
    global search

    # Initialize user interface
    userInterface = UserInterface(fileName = fileName)

    scrape()
    if not os.path.exists("data/saved-webscrape.txt"):
        pickle = PickleToFile("data/saved-webscrape.txt")
        pickle.pickleObjectToFile(factory.webData)

    search = Search(userInterface, factory.textData.keys(), factory.webData)

@app.route('/multi/combine', methods = ['PUT'])
def find_combine():
    global multi
    multi = 'combine'
    return json.dumps({'success':True}), 200, {'Content-Type':'application/json'}

@app.route('/multi/filter', methods = ['PUT'])
def find_filter():
    global multi
    multi = 'filter'
    return json.dumps({'success':True}), 200, {'Content-Type':'application/json'}

@app.route('/find/<category>', methods = ['POST', 'GET'])
def find(category):
    global search
    global factory
    global results
    global multi

    if request.method == 'GET':
        switch = {
                'weight' : 1,
                'department' : 2,
                'code' : 3,
                'semester' : 4,
                'level' : 5,
                'full_course_code' : 6,
                'availability' : 7,
                'faculty' : 8,
                'dropped' : 9,
                'not_in_current_semester' : 10,
                'capacity_maximum' : 11,
                'capacity_minimum' : 12,
            }


        data = request.args
        term = None
        if 'term' in data:
            term = data['term']
        elif category != 'dropped' and category != 'not_in_current_semester':
            abort(400)

        matches = []
        matches = search.findKeys(params=[switch.get(category), term])

        if multi != None and results != None:
            # using filter, keep only matches of keys that are in the initial search and the new search
            if multi == 'filter':
                matches = list(filter(lambda key: key in matches, results))
            # using a set type, keep all unique matches (remove duplicates) that are in the initial search and the new search
            elif multi == 'combine':
                matches = list(set(matches + results))

        results = matches
        multi = None

        return factory.to_json(matches), 200, {'Content-Type':'application/json'}

@app.route('/export/<filename>', methods = ['POST'])
def export(filename):
    global factory
    global results

    if results == None:
        return json.dumps({'success':False,'Description':'No search results to export'}), 428, {'Content-Type':'application/json'}
    exporter = Exporter(factory.to_dict(results), factory.webData, factory.textData, filename)
    exporter.export()

    return json.dumps({'success':True}), 200, {'Content-Type':'application/json'}

@app.route('/get/<category>', methods = ['GET'])
def getData(category):
    global factory

    data = request.args
    term = None
    if 'term' in data:
        term = data['term']

    if category == 'faculty':
        array = []
        for key, course in factory.webData.items():
            if course.get_faculty() not in array:
                array.append(course.get_faculty())

        dictionaryVersion = {i: array[i] for i in range(0, len(array))}
        return dictionaryVersion, 200, {'Content-Type':'application/json'}

    elif category == 'allCourseCodes':
        array = []
        for key in factory.textData.keys():
            if factory.textData[key].coursecode not in array:
                array.append(factory.textData[key].coursecode)

        dictionaryVersion = {i: array[i] for i in range(0, len(array))}
        return dictionaryVersion, 200, {'Content-Type':'application/json'}

    elif category == 'exportFiles':
        data_dir = os.path.dirname(os.getcwd()) + '/backend/export/'
        array = [f for f in os.listdir(data_dir) if fnmatch.fnmatch(f, '*.csv')]
        
        fileNames = {name.replace('Edges', '').replace('Nodes', '').replace('Table', '').replace('.csv', '') for name in array}
        keys = {i for i in range(0, len(fileNames))}
        return  dict(zip(keys, fileNames)), 200, {'Content-Type':'application/json'}

    elif category == 'edges':
        if term is None:
            return json.dumps({'success':False,'Description':'File not provided'}), 400, {'Content-Type':'application/json'}

        edgeFile = term
        if not edgeFile.startswith('Edges'):
            edgeFile = 'Edges' + edgeFile
        if not edgeFile.endswith('Table.csv'):
            edgeFile = edgeFile + 'Table.csv'

        edgeDicts = factory.csv_to_dicts(edgeFile)
        if edgeDicts is None:
            return json.dumps({'success':False,'Description':'File not found {}'.format(edgeFile)}), 404, {'Content-Type':'application/json'}

        returnData = []
        for data in edgeDicts:
            returnData.append({
                'Source' : data['Source'],
                'Target' : data['Target']
            })

        return json.dumps({'links': returnData}), 200, {'Content-Type':'application/json'}


    elif category == 'nodes':
        if term is None:
            return json.dumps({'success':False,'Description':'File not provided'}), 400, {'Content-Type':'application/json'}

        nodeFile = term
        if not nodeFile.startswith('Nodes'):
            nodeFile = 'Nodes' + nodeFile

        if not nodeFile.endswith('Table.csv'):
            nodeFile = nodeFile + 'Table.csv'

        nodeDicts = factory.csv_to_dicts(nodeFile)
        if nodeDicts is None:
            return json.dumps({'success':False,'Description':'File not found {}'.format(nodeFile)}), 404, {'Content-Type':'application/json'}

        returnData = []
        for data in nodeDicts:
            dictData = {           
                'Id' : data['Id'],
                'Label' : data['Label'],
                'Department': data['Department'],
                'Status': data['Status'],
                'In Dataset': data['In Dataset']
            }

            course = Course.Find(data['Id'], factory.textData)
            if course != None:
                webKey = course.webKey
                courseInfo = course.to_dict(factory.webData)
                dictData['Semesters'] = courseInfo['semesters']
                dictData['Weight'] = courseInfo['weight']
                dictData['Title'] = courseInfo['title']
                dictData['Description'] = courseInfo['description']
                dictData['Restrictions'] = courseInfo['restrictions'] if courseInfo['restrictions'] else 'None'
                dictData['Prerequisites'] = courseInfo['prereqs'] if courseInfo['prereqs'] else 'None'

                if 'availability' in courseInfo:
                    dictData['availability'] = courseInfo['availability']

                if 'capacity' in courseInfo:
                    dictData['capacity'] = courseInfo['capacity']

                if 'faculty' in courseInfo:
                    dictData['faculty'] = courseInfo['faculty']

            returnData.append(dictData)

        return json.dumps({'nodes': returnData}), 200, {'Content-Type':'application/json'}
    
    else:
        abort(400)

@app.route('/exportEdges', methods = ['GET'])
def exportEdges():
    global factory
    global results

    if results == None:
        return json.dumps({'success':False,'Description':'No search results to export'}), 428, {'Content-Type':'application/json'}
    exporter = Exporter(factory.to_dict(results), factory.webData, factory.textData, "")
    exporter.exportEdges()

    return exporter.edges, 200, {'Content-Type':'application/json'}

@app.route('/exportNodes', methods = ['GET'])
def exportNodes():
    global factory
    global results

    if results == None:
        return json.dumps({'success':False,'Description':'No search results to export'}), 428, {'Content-Type':'application/json'}
    exporter = Exporter(factory.to_dict(results), factory.webData, factory.textData, "")
    exporter.exportEdges() # Required to populate the export.edges data, which exportNodes uses to check for duplicates
    exporter.exportNodes()

    return exporter.nodes, 200, {'Content-Type':'application/json'}

def main():
    global search
    global factory
    global userInterface

    init()
    # gameloop
    while 1:
        # perform search with the user interface and get all the keys that match
        search = Search(userInterface, factory.textData.keys(), factory.webData)
        matches = search.findKeys()

        # if the user wants to quit exit the loop
        if (matches == 'quit'):
            break

        # post search, ask if the user wants to further filter/combine their search
        multi, type_multi = userInterface.multisearch()

        #This is checking if it is option 10, since we cant check attributes of hash table
        #inside search need to do it out here after all searching is done
        isOption10 = False
        if search.termType == 'Not in current semester':
            isOption10 = True

        while multi:
            new_keys = search.findKeys()

            # using filter, keep only matches of keys that are in the initial search and the new search
            if type_multi == 'filter':
                matches = list(filter(lambda key: key in new_keys, matches))
            # using a set type, keep all unique matches (remove duplicates) that are in the initial search and the new search
            elif type_multi == 'combine':
                matches = list(set(matches + new_keys))

            if (search.termType == 'Not in current semester'):
                isOption10 = True

            # post search, ask if the user wants to further filter/combine their search
            multi, type_multi = userInterface.multisearch()

        #once all the searching is done need to shorten the list to courses that should be offered
        #in the current semester but arn't
        if (isOption10):
            newMatches = []
            for key in matches:
                if (factory.textData[key].webKey == None):
                    newMatches.append(key)
            matches = newMatches

        # output search result to the user and ask if they want to export the data
        # generate course output
        totalString = ""
        for match in matches:
            currentCourse = factory.textData[match]
            out = str(currentCourse)
            if (currentCourse.webKey != None):
                out += "\nStatus: " + factory.webData[currentCourse.webKey].get_status() + "\nAvailability: " + str(factory.webData[currentCourse.webKey].get_availability()) + "\nCapacity: " + str(factory.webData[currentCourse.webKey].get_capacity()) + "\nFaculty: " + factory.webData[currentCourse.webKey].get_faculty()
            else:
                out += "\nStatus: Not Available Winter (NAW)"
            totalString = totalString + out + "\n\n"

        # check if user wants to export their data
        resp, exp_filename = userInterface.export()
        if resp != 'no':
            match_courses = {}

            # if they want to export only search results or all course data, generate dictionary with courses
            if resp == 'search':
                for match in matches:
                    match_courses[match] = factory.textData[match]
            else:
                match_courses = factory.textData

            # export the course data with the given filename
            exporter = Exporter(match_courses, factory.webData, factory.textData, exp_filename)
            exporter.export()


        # output search results to the user
        userInterface.output_query(totalString)

init('course-descriptions.txt')
if __name__ == "__main__":
    app.run()

    # For deploying with WSGI later
    #https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/
    #https://www.youtube.com/watch?v=x6SvecADw2M
