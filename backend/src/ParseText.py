from .Course import Course

def parser(fileName):
    data = ""
    hashTableOfCourses = {}
    try:
        with open(fileName, 'r', encoding="utf8", errors='ignore') as file:
            data = file.read()
    except:
        print("File does not exist")
        return {}

    wordArr = data.split()

    #Finds the starting point
    startingPoint = 0
    for i in range(len(wordArr)):
        if (wordArr[i] == "Descriptions,"):
            startingPoint = i
            break

    #Begin parsing
    i = startingPoint
    while i + 1 < len(wordArr):
        i = i + 1
        # Uses the * char to find the course to parse
        if "*" in wordArr[i]:
            courseCode = wordArr[i]
            title = ""
            i = i + 1

            # Takes parser to the end of the course title
            while "(" not in wordArr[i]:
                if title == "":
                    title = wordArr[i]
                else:
                    title = title + " " + wordArr[i]
                i = i + 1
            i = i - 1

            # When using '(' to find title an extra char is added so need to remove it
            title = " ".join(title.split(" ")[:-1])
            semestersOffered = wordArr[i]

            # Moves parser to the course weight (denoted as [0.5])
            while "[" not in wordArr[i]:
                i = i + 1
            courseWeight = wordArr[i]
            courseWeight = courseWeight[1:]
            courseWeight = courseWeight[:-1]
            i = i + 1
            description = ""

            # When parser gets to one of the following words it will be the end of the course description
            while ((wordArr[i] != "Prerequisite(s):") and (wordArr[i] != "Offering(s):") and (wordArr[i] != "Equate(s):") and (wordArr[i] != "Restriction(s):") and (wordArr[i] != "Department(s):")):
                if description == "":
                    description = wordArr[i]
                else:
                    description = description + " " + wordArr[i]
                i = i + 1

            # Of the following words department is always last, finishes created object
            # after parsing the department
            atDepartment = 0
            preReqs = ""
            restrictions = ""
            department = ""
            equates = ""
            offerings = ""
            while atDepartment != 1:

                # Gathers the prerequisites for the course
                if wordArr[i] == "Prerequisite(s):":
                    i = i + 1
                    while ((wordArr[i] != "Prerequisite(s):") and (wordArr[i] != "Offering(s):") and (wordArr[i] != "Equate(s):") and (wordArr[i] != "Restriction(s):") and (wordArr[i] != "Department(s):")):
                        if preReqs == "":
                            preReqs = wordArr[i]
                        else:
                            preReqs = preReqs + " " + wordArr[i]
                        i = i + 1

                # Gathers the restrictions for the course
                if wordArr[i] == "Restriction(s):":
                    i = i + 1
                    while ((wordArr[i] != "Prerequisite(s):") and (wordArr[i] != "Offering(s):") and (wordArr[i] != "Equate(s):") and (wordArr[i] != "Restriction(s):") and (wordArr[i] != "Department(s):")):
                        if restrictions == "":
                            restrictions = wordArr[i]
                        else:
                            restrictions = restrictions + " " + wordArr[i]
                        i = i + 1

                # Gathers the department for the course, flags for the loop to end
                # as department is always last
                if wordArr[i] == "Department(s):":
                    atDepartment = 1
                    i = i + 1

                    # The department section will end at either the start of the next course or a newline
                    while (wordArr[i] != "\n" and ("*" not in wordArr[i]) and ("." not in wordArr[i]) and (wordArr[i] != "Location(s):")) or (i + 1) == len(wordArr):
                        if (i + 1) == len(wordArr):
                            break
                        if department == "":
                            department = wordArr[i]
                        else:
                            department = department + " " + wordArr[i]
                        i = i + 1
                    if (i + 1) == len(wordArr):
                        break
                    i = i - 1
                i = i + 1

            # Creating the course as a class then adding it to the hashtable if it isn't in the table already
            courseToAdd = Course(semestersOffered, courseWeight, title, department, courseCode, description, restrictions, preReqs)

            # Check uniqueness of course code (faulty file fool proof method)
            dict_keys = hashTableOfCourses.keys()
            unique = True
            for key in dict_keys:
                course_code = courseToAdd.coursecode.split("*")
                key_partial = course_code[0] + "-" + course_code[1]
                if key_partial in key:
                    unique = False
                    break

            if unique:
                hashTableOfCourses[courseToAdd.to_hash()] = courseToAdd

            i = i - 1
    return hashTableOfCourses
