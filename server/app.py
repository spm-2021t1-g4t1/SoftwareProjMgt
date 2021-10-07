
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

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/lms'


@app.route('/staff')
def list_of_staff():
    return staff.get_staffList()


@app.route('/enrolment/<int:course_id>/<int:class_no>')
def getClasslist(course_id,class_no):
    return classEnrolment.getClasslist(course_id,class_no)

@app.route('/enrolment/<string:staff_username>')
def getStaff_Enrollment(staff_username):
    classEnrolments = {'data':[]}
    ClassList = classEnrolment.getStaffEnrollment(staff_username)

    for classesObj in ClassList['data'].values():
        # print(classesObj)
        Courses = course.get_specificCourse(classesObj['course_id'])['data']
        classObj = classes.get_specificClass(classesObj['course_id'],classesObj['class_no'])['data']
        
        classEnrolments['data'].append({
            'course_id' : Courses['course_id'],
            'course_name': Courses['course_name'],
            'description': Courses['description'],
            'classes': [classObj]
        })

    return classEnrolments

@app.route('/course')
def get_all_course():
    return course.get_listOfCourse()

@app.route('/course/<int:course_id>')
def get_one_course(course_id):
    return course.get_specificCourse(course_id)

@app.route('/course/<int:course_id>/<int:class_no>')
def get_specificCourseDetail(course_id,class_no):
    ClassDetail = {'data':[]}

    Courses = course.get_specificCourse(course_id)['data']
    classObj = classes.get_specificClassDetail(course_id,class_no)['data']
        
    ClassDetail['data'] ={
            'course_id' : Courses['course_id'],
            'course_name': Courses['course_name'],
            'description': Courses['description'],
            "learning_objective": Courses['learning_objective'],
            'classes': [classObj]
    }
    return ClassDetail

@app.route('/lesson/<int:course_id>/<int:class_no>/<string:staff_username>') ######
def get_lessons(course_id, class_no, staff_username):
    ClassDetail = {'data':[]}

    Courses = course.get_specificCourse(course_id)['data']
    classObj = classes.get_specificClassDetail(course_id,class_no)['data']
        

    all_lessons = lesson.get_allLessonByClass(course_id, class_no)['data']
    LessonDetail = {'data': []}
    LessonDetail['data'].append(all_lessons[0])
    curr_index = 0
    for each_lesson in all_lessons:
        material_count_for_current_lesson = len(each_lesson['lesson_materials'])
        list_of_material_viewed_by_staff = materials_viewed.get_listOfMaterialsViewedByStaff(course_id, class_no, each_lesson['lesson_no'], staff_username)['data']
        if material_count_for_current_lesson == len(list_of_material_viewed_by_staff) and material_count_for_current_lesson != 0:
            current_staff_quiz_score = quiz_attempts.get_listOfQuizAttemptsByStaff(course_id, class_no, staff_username)['data']['quiz_score']
            if current_staff_quiz_score >= 80 and curr_index+1 < len(all_lessons):   
                LessonDetail['data'].append(all_lessons[curr_index+1])
        curr_index = curr_index + 1
    
    classObj['lesson'] = LessonDetail['data']
    ClassDetail['data'] ={
            'course_id' : Courses['course_id'],
            'course_name': Courses['course_name'],
            'description': Courses['description'],
            "learning_objective": Courses['learning_objective'],
            'classes': [classObj]
    }
    
    
    return ClassDetail




@app.route('/quiz', methods=['POST', 'GET'])
def get_all_quiz():
    return Quiz.get_listofQuiz()

@app.route('/quiz/<int:quiz_id>', methods=['POST', 'GET'])
def get_spec_quiz(quiz_id):
    return Quiz.get_quiz_details(quiz_id)


@app.route('/quiz_ques/<int:qid>', methods=['POST', 'GET'])
def get_all_ques(qid):
    # return json.loads(str(Question.get_courseQues(qid)))
    return Question.get_courseQues(qid)

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
    #just python app.py to execute
