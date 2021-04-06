class WebCourse:
    #This is under the assumption that were only looking for winter courses.
    def __init__(self,weight,title,department,coursecode,status,faculty,capacity):
        self.weight = weight
        self.title = title
        self.department = department
        self.coursecode = coursecode
        self.status = status
        self.faculty = faculty
        self.capacity = capacity
        self.courseKey = None

    def __str__(self):
        return("Course Title: " + self.title + "\nCourse Code: " + self.coursecode + "\nCourse Weight: " + self.weight + "\nDepartment: " + self.department + "\nStatus: " + self.status + "\nFaculty: " +  self.faculty + "\nCapacity: " + self.capacity + "\n")

    def get_status(self):
        return(self.status)

    def get_availability(self):
        availabilitySplit = self.capacity.split("/")
        return(int(availabilitySplit[0]))

    def get_capacity(self):
        capacitySplit = self.capacity.split("/")
        return(int(capacitySplit[1]))

    def get_faculty(self):
        return(self.faculty)

    #Course code on the txt file is formatted ex: CIS*2750
    def to_hash(self):
        keyValues = self.coursecode.split("*")
        text = keyValues[0] + "-" + keyValues[1]
        return text
