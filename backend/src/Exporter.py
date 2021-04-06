import os
import json

import src.Course
class Exporter:

    def __init__(self, course_dict, web_dict, full_course_dict, file_name):
        self._course_dict = course_dict
        self.full_course_dict = full_course_dict
        self.web_dict = web_dict

        self._file_name = file_name

        self.edges = []
        self.nodes = []

        data_dir = os.path.dirname(os.getcwd()) + '/backend/export/'
        self._edge_file = data_dir + "Edges" + self._file_name + "Table.csv"
        self._node_file = data_dir + "Nodes" + self._file_name + "Table.csv"

    # Pre: Edge table file is not created, or an old one exists that will be overwritten
    # Post: Edge table CSV file is created with connections to every course
    def __exportEdgeTable(self):
        file = open(self._edge_file,"w+")
        file.write("Source,Target\n")

        # Search through every course
        for _, course in self._course_dict.items():
            target = course.coursecode
            sources = course.prereqs.split()

            # Search through the course's requirements
            for prereq in sources:

                # If an asterisk in prereq list, we know this is contains a valid prereq course so we add it to our export results
                if "*" in prereq:

                    # We must sanitize some of the data
                    line = prereq.replace(',', '').replace(';', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('.', '').replace('.', '') + "," + target.replace(',', '').replace('(', '').replace(')', '').replace(']', '').replace('[', '').replace('.', '').replace('.', '') + "\n"
                    file.write(line)

        file.close()


    # Pre: Node table is not created, or an old one exists that will be overwritten
    # Post: Node table CSV file is created with connections to every course
    def __exportNodeTable(self):
        # Get all course codes from the edges table
        file = open(self._edge_file, "r")
        lines = file.readlines()
        codes = []

        # Iterate through edge table skipping header
        for line in lines[1:]:
            split = line.split(',')
            if split[0] not in codes:
                codes.append(split[0])

        file.close()


        file = open(self._node_file,"w+")
        file.write("Id,Label,Department,Status,In Dataset\n")

        # Search through each course in the export dictionary
        for _, course in self._course_dict.items():

            coursecode = course.coursecode.replace(',', '').replace(';', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('.', '').replace('.', '').replace('credits', '').replace('(', '').replace('Management', '')

            # Prevent duplicate course codes from being entered as nodes in the table
            if coursecode in codes:
                codes.remove(coursecode)

            webKey = course.webKey
            status = " - NAW"
            if (webKey != None):
                status = " - " + self.web_dict[webKey].get_status()
            line = coursecode + ",\"" + coursecode + status + "\",\"" + course.coursecode.split('*')[0].replace('credits', '').replace('(', '').replace('Management', '') + "\"" + ",\"" + status.replace(" - ", "") + "\",\"Yes\"\n"
            file.write(line)

        # Add any course code from edge table that isn't in the dictionary (e.g. discontinued courses with edges connecting to them as prereqs)
        # (doesn't mean the course doesn't exist, might be because node was filtered out with a search)
        for course in codes:
            webKey = course.replace("*", "-")
            
            webCourse = self.web_dict.get(webKey, None)
            webStatus = " - NAW"
            if (webCourse != None):
                webStatus = " - " + webCourse.get_status()
            line = course + ",\"" + course + webStatus + ' (Not in Dataset)' + "\",\"" + course.split('*')[0].replace('credits', '').replace('(', '').replace('Management', '') + "\"" + ",\"" + webStatus.replace(" - ", "") + "\",\"No\"\n"
            file.write(line)


        file.close()


    # Pre: Edge table data is unknown
    # Post: Edge table data is returned as a JSON object
    def __exportEdgeTableAsJson(self):
        returnData = []

        # Search through every course
        for _, course in self._course_dict.items():
            target = course.coursecode
            sources = course.prereqs.split()

            # Search through the course's requirements
            for prereq in sources:

                # If an asterisk in prereq list, we know this is contains a valid prereq course so we add it to our export results
                if "*" in prereq:

                    # We must sanitize some of the data
                    source = prereq.replace(',', '').replace(';', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('.', '').replace('.', '')
                    target = target.replace(',', '').replace('(', '').replace(')', '').replace(']', '').replace('[', '').replace('.', '').replace('.', '')
                    returnData.append({
                        'Source' : source,
                        'Target' : target
                    })

        self.edges = json.dumps({'links': returnData})
        return self.edges


    # Pre: Node table data is unknown
    # Post: Node table data is returned as a JSON object
    def __exportNodeTableAsJson(self):
        # Get all course codes from the edges table
        codes = []
        returnData = []

        # Iterate through edge table skipping header
        edges = json.loads(self.edges)
        for item in edges:
            for edge in edges[item]:
                if edge['Source'] not in codes:
                    codes.append(edge['Source'])

        # Search through each course in the export dictionary
        for _, course in self._course_dict.items():

            coursecode = course.coursecode.replace(',', '').replace(';', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('.', '').replace('.', '').replace('credits', '').replace('(', '').replace('Management', '')

            # Prevent duplicate course codes from being entered as nodes in the table
            if coursecode in codes:
                codes.remove(coursecode)

            webKey = course.webKey
            courseInfo = course.to_dict(self.web_dict)
            status = " - NAW"
            if (webKey != None):
                status = " - " + self.web_dict[webKey].get_status()
            label = coursecode + status
            department =  course.coursecode.split('*')[0].replace('credits', '').replace('(', '').replace('Management', '')
            status = status.replace(" - ", "")
            dictData = {           
                'Id' : coursecode,
                'Label' : label,
                'Department': department,
                'Status': status,
                'In Dataset': 'Yes',
                'Semesters': courseInfo['semesters'],
                'Weight': courseInfo['weight'],
                'Title': courseInfo['title'],
                'Description': courseInfo['description'],
                'Restrictions': courseInfo['restrictions'] if courseInfo['restrictions'] else 'None',
                'Prerequisites': courseInfo['prereqs'] if courseInfo['prereqs'] else 'None'
            }

            if 'availability' in courseInfo:
                dictData['availability'] = courseInfo['availability']

            if 'capacity' in courseInfo:
                dictData['capacity'] = courseInfo['capacity']

            if 'faculty' in courseInfo:
                dictData['faculty'] = courseInfo['faculty']

            returnData.append(dictData)

        # Add any course code from edge table that isn't in the dictionary (e.g. discontinued courses with edges connecting to them as prereqs)
        # (doesn't mean the course doesn't exist, might be because node was filtered out with a search)
        for course in codes:
            webKey = course.replace("*", "-")
            webCourse = self.web_dict.get(webKey, None)

            courseObj = None
            webStatus = " - NAW"
            if (webCourse != None):
                webStatus = " - " + webCourse.get_status()
                if webCourse.courseKey != None:
                    courseObj = self.full_course_dict[webCourse.courseKey]

            label = course + webStatus + ' (Not in Dataset)'
            department = course.split('*')[0].replace('credits', '').replace('(', '').replace('Management', '')
            status =  webStatus.replace(" - ", "")
            dictData = {
                'Id' : course,
                'Label' : label,
                'Department': department,
                'Status': status,
                'In Dataset': 'No'
            }

            if courseObj != None:
                courseInfo = courseObj.to_dict(self.web_dict)
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

        self.nodes = json.dumps({'nodes': returnData})
        return self.nodes


    # Pre: User has requested an export from their search
    # Post: Nodes and Edges CSV files are produced with export data to import into Gephi
    def export(self):
        self.__exportEdgeTable()
        self.__exportNodeTable()


    # Pre: User has requested an Edges table export from their search
    # Post: Edges table is returned in JSON format
    def exportEdges(self):
        self.edges = self.__exportEdgeTableAsJson()
    

    # Pre: User has requested a Nodes table export from their search
    # Post: Nodes table is returned in JSON format
    def exportNodes(self):
        self.nodes = self.__exportNodeTableAsJson()
