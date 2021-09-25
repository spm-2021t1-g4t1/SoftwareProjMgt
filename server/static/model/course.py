class Course():
    def __init__(self, code,  title, description, learningObjective):
        self.code = code
        self.title = title
        self.description = description
        self.learningObjective = learningObjective
        self.Class = []

    def getCourseCode(self):
        return self.code

    def getCourseTitle(self):
        return self.title

    def getCourseDescription(self):
        return self.description

    def getlearningObjective(self):
        return self.learningObjective

    def addClass(self, Class):
        self.Class.append(Class)


class Class():
    def __init__(self, startDate,  endDate, startTime, endTime, classSize, instructor):
        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime
        self.classSize = classSize
        self.instructor = instructor
        self.section - []
    
    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def getClassSize(self): 
        return self.classSize

    def getInstructor(self):
        return self.instructor

    def addSection(self, section):
        self.section.append(section)


class Section():
    def __init__(self,  sectionCode, name, description):
        self.sectionCode = sectionCode
        self.name = name
        self.description = description
        self.courseMaterial = []

    def getStartDate(self):
        return self.sectionCode

    def getEndDate(self):
        return self.name

    def getStartTime(self):
        return self.description

    def getEndTime(self):
        return self.courseMaterial

    def addccourseMaterial