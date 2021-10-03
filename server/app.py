
#Import external modules
from flask import Flask
from db import db
from flask_cors import CORS

#Import your classes here
from static.model.staff import *
from static.model.course import *


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'

@app.route('/staff')
def list_of_staff():
    return course.get_staffList()


@app.route('/enrolment/<int:course_id>/<int:class_no>')
def getClasslist(course_id,class_no):
    return classEnrolment.getClasslist(course_id,class_no)

@app.route('/enrolment/<string:staff_username>')
def getStaff_Username(staff_username):
    classEnrolments = {'data':{}}
    ClassList = classEnrolment.getStaffEnrollment(staff_username)

    for classesObj in ClassList['data'].values():
        # print(classesObj)
        Courses = course.get_specificCourse(classesObj['course_id'])['data']
        classObj = classes.get_specificClass(classesObj['course_id'],classesObj['class_no'])['data']
        
        classEnrolments['data'][Courses['course_id']] = {
            'course_id' : Courses['course_id'],
            'course_name': Courses['course_name'],
            'description': Courses['description'],
            'class': classObj
        }

    return classEnrolments



@app.route('/course')
def get_all_course():
    return course.get_listOfCourse()

@app.route('/course/<int:course_id>')
def get_one_course(course_id):
    return course.get_specificCourse(course_id)

@app.route('/course/<int:course_id>/<int:class_no>')
def get_all_class(course_id,class_no):
    return classes.get_specificClass(course_id,class_no)



if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
    #just python app.py to execute
