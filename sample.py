from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'
db = SQLAlchemy(app)

class Course():
    __tablename__ ="course_enrolment"
    course_id = db.Column(db.String(255), primary_key=True)
    coure_name = db.Column(db.Integer, primary_key=True)
    

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
    def __init__(self, courseId, classNo ,startDate,  endDate, startTime, endTime, classSize, instructor):
        self.courseId = courseId
        self.classNo = classNo
        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime
        self.classSize = classSize
        self.instructor = instructor
        self.section - []

    def getCourseId(self):
        return self.courseId

    def getClassNo(self):
        return self.ClassNo

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


class Lesson():
    def __init__(self, courseId, classNo, sectionCode, name, description):
        self.CourseId = courseId
        self.ClassNo = classNo
        self.sectionCode = sectionCode
        self.name = name
        self.description = description
        self.courseMaterial = []

    def getSectionCode(self):
        return self.sectionCode

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getCourseMaterial(self):
        return self.courseMaterial

    def addCourseMaterial(self, material):
        try:
            self.courseMaterial.append(material)
            return True
        except:
            return False

