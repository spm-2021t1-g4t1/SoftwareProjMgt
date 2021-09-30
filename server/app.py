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
def testing(course_id,class_no):
    return classEnrolment.getClasslist(course_id,class_no)




@app.route('/course')
def get_all_course():
    return course.get_listOfCourse()

@app.route('/course/<int:course_id>')
def get_one_course(course_id):
    return course.get_specificCourse(course_id)






if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
    #just python app.py to execute
