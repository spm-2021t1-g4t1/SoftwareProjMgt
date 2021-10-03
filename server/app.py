
#Import external modules
from flask import Flask
from db import db
from flask_cors import CORS
import json


#Import your classes here
from static.model.staff import *
from static.model.course import *
from static.model.quiz import *



app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/lms'


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

@app.route('/quiz', methods=['POST', 'GET'])
def get_all():
    quiz = Quiz.query.all()
    json_thing = {
        "code": 200,
        "data": {
            "quiz": [q.json() for q in quiz]
        }
    }
    return json.dumps(json_thing, default=str)

@app.route('/quiz_ques/<int:qid>', methods=['POST', 'GET'])
def get_all_ques(qid):
    ques = Question.query.filter_by(qid=qid).all()
    json_thing = {
        "code": 200,
        "data": {
            "ques": [q.json() for q in ques]
        }
    }

    return json.dumps(json_thing, default=str)

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
    #just python app.py to execute
